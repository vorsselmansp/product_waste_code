# -*- coding: utf-8 -*-

from odoo import models, fields, api


class product_waste_code(models.Model):
    _name = 'product_waste_code.product_waste_code'
    _order = 'sequence,id'
    _description = 'product_waste_code.product_waste_code'
    #_parent_name = 'product_waste_code'                  # by default its name is parent_id you can change it
    #_parent_store = True                                    # tell odoo that this model support parent & child relation ship


    title = fields.Char(string='Title')
    chapter = fields.Char(string='Chapter')
    subchapter1 = fields.Char(string='Sub chapter 1')
    subchapter2 = fields.Char(string='Sub chapter 2')
    description = fields.Char(string='Description')
    examples = fields.Text(string='Example')
    info = fields.Text()
    company_info = fields.Text(company_dependent=True)
    display_info = fields.Text(string='Infos', compute='_compute_display_info')
    state = fields.Selection(selection=[
           ('draft', 'Draft'),
           ('in_review', 'In Review'),
           ('rejected', 'Rejected'),
           ('final', 'Final State'),
       ], string='Status', required=True, readonly=False, copy=False,
       tracking=True, default='draft')

    name = fields.Char(string='Name')

    sequence = fields.Integer(default=10)
#    res_model = fields.Selection(related="plan_id.res_model")
    #company_id = fields.Many2one(related='company_id')
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    chapter_title = fields.Many2one('product_waste_code.product_waste_code', string='Chapter Title')
    chapter_label = fields.Text(string='chapter_label', compute='_compute_chapter_label',  )
    subchapter1_label =  fields.Text(string="subchapter1_label", compute='_compute_subchapter1_label')
    subchapter2_label =  fields.Text(string="subchapter2_label", compute='_compute_subchapter2_label')

    subchapter1_title = fields.Many2one('product_waste_code.product_waste_code', string='Subchapter 1 Title')

    # toggles the global visibility of the record, if active is set to False the record is invisible in most searches and listing.
    active = fields.Boolean()

    # note = fields.Html('Note', compute="_compute_note", store=True, readonly=False)

    @api.depends('chapter', 'title', 'subchapter1', 'subchapter2')
    def _compute_chapter_label(self):
        for record in self:
            # Only select the records where the chapter matches
            matching_records = self.env['product_waste_code.product_waste_code'].search([('chapter', '=', record.chapter)])
            
            if matching_records:
                for match in matching_records:
                    if match.subchapter1 == "" and match.subchapter2 == "":
                        record.chapter_label = match.title

            else:
                record.chapter_label = "not found->" + record.chapter + record.subchapter1 + record.subchapter2 + str(matching_records)
    
    @api.depends('chapter', 'title', 'subchapter1', 'subchapter2')
    def _compute_subchapter1_label(self):
        for record in self:
            # Only select the records where the chapter matches
            matching_records = self.env['product_waste_code.product_waste_code'].search([('chapter', '=', record.chapter)])
            
            if matching_records:
                for match in matching_records:
                    if match.subchapter1 == self.subchapter1 and match.subchapter2 == "":
                        record.subchapter1_label = match.title
            else:
                record.subchapter1_label = "not found->" + record.chapter + record.subchapter1 + record.subchapter2 + str(matching_records)
    
    @api.depends('chapter', 'title', 'subchapter1', 'subchapter2')
    def _compute_subchapter2_label(self):
        for record in self:
            # Only select the records where the chapter matches
            matching_records = self.env['product_waste_code.product_waste_code'].search([('chapter', '=', record.chapter)])
            
            if matching_records:
                for match in matching_records:
                    if match.subchapter1 == self.subchapter1 and match.subchapter2 == self.subchapter2:
                        record.subchapter2_label = match.title
            else:
                record.subchapter2_label = "not found->" + record.chapter + record.subchapter1 + record.subchapter2 + str(matching_records)

        

    def button_in_progress(self):
       self.write({
           'state': "final"
        })

    @api.depends_context('company')
    def _compute_display_info(self):
        for record in self:
            record.display_info = record.info + record.company_info
            
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

