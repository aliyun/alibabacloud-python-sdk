# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MealApplyAddShrinkRequest(DaraModel):
    def __init__(
        self,
        apply_user_shrink: str = None,
        cost_center_id: int = None,
        extend_field: str = None,
        invoice_id: int = None,
        itinerary_list_shrink: str = None,
        meal_amount: int = None,
        meal_cause: str = None,
        project_code: str = None,
        project_title: str = None,
        status: int = None,
        third_part_apply_id: str = None,
        third_part_cost_center_id: str = None,
        third_part_invoice_id: str = None,
    ):
        # This parameter is required.
        self.apply_user_shrink = apply_user_shrink
        self.cost_center_id = cost_center_id
        self.extend_field = extend_field
        self.invoice_id = invoice_id
        # This parameter is required.
        self.itinerary_list_shrink = itinerary_list_shrink
        self.meal_amount = meal_amount
        # This parameter is required.
        self.meal_cause = meal_cause
        self.project_code = project_code
        self.project_title = project_title
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.third_part_apply_id = third_part_apply_id
        self.third_part_cost_center_id = third_part_cost_center_id
        self.third_part_invoice_id = third_part_invoice_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_user_shrink is not None:
            result['apply_user'] = self.apply_user_shrink

        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id

        if self.extend_field is not None:
            result['extend_field'] = self.extend_field

        if self.invoice_id is not None:
            result['invoice_id'] = self.invoice_id

        if self.itinerary_list_shrink is not None:
            result['itinerary_list'] = self.itinerary_list_shrink

        if self.meal_amount is not None:
            result['meal_amount'] = self.meal_amount

        if self.meal_cause is not None:
            result['meal_cause'] = self.meal_cause

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.status is not None:
            result['status'] = self.status

        if self.third_part_apply_id is not None:
            result['third_part_apply_id'] = self.third_part_apply_id

        if self.third_part_cost_center_id is not None:
            result['third_part_cost_center_id'] = self.third_part_cost_center_id

        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_user') is not None:
            self.apply_user_shrink = m.get('apply_user')

        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('extend_field') is not None:
            self.extend_field = m.get('extend_field')

        if m.get('invoice_id') is not None:
            self.invoice_id = m.get('invoice_id')

        if m.get('itinerary_list') is not None:
            self.itinerary_list_shrink = m.get('itinerary_list')

        if m.get('meal_amount') is not None:
            self.meal_amount = m.get('meal_amount')

        if m.get('meal_cause') is not None:
            self.meal_cause = m.get('meal_cause')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('third_part_apply_id') is not None:
            self.third_part_apply_id = m.get('third_part_apply_id')

        if m.get('third_part_cost_center_id') is not None:
            self.third_part_cost_center_id = m.get('third_part_cost_center_id')

        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')

        return self

