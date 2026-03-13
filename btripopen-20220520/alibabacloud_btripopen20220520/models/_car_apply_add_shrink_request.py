# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CarApplyAddShrinkRequest(DaraModel):
    def __init__(
        self,
        cause: str = None,
        city: str = None,
        city_code_set: str = None,
        date: str = None,
        finished_date: str = None,
        project_code: str = None,
        project_name: str = None,
        status: int = None,
        third_part_apply_id: str = None,
        third_part_cost_center_id: str = None,
        third_part_invoice_id: str = None,
        times_total: int = None,
        times_type: int = None,
        times_used: int = None,
        title: str = None,
        traveler_standard_shrink: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.cause = cause
        # This parameter is required.
        self.city = city
        self.city_code_set = city_code_set
        # This parameter is required.
        self.date = date
        self.finished_date = finished_date
        self.project_code = project_code
        self.project_name = project_name
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.third_part_apply_id = third_part_apply_id
        self.third_part_cost_center_id = third_part_cost_center_id
        self.third_part_invoice_id = third_part_invoice_id
        # This parameter is required.
        self.times_total = times_total
        # This parameter is required.
        self.times_type = times_type
        # This parameter is required.
        self.times_used = times_used
        # This parameter is required.
        self.title = title
        self.traveler_standard_shrink = traveler_standard_shrink
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cause is not None:
            result['cause'] = self.cause

        if self.city is not None:
            result['city'] = self.city

        if self.city_code_set is not None:
            result['city_code_set'] = self.city_code_set

        if self.date is not None:
            result['date'] = self.date

        if self.finished_date is not None:
            result['finished_date'] = self.finished_date

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_name is not None:
            result['project_name'] = self.project_name

        if self.status is not None:
            result['status'] = self.status

        if self.third_part_apply_id is not None:
            result['third_part_apply_id'] = self.third_part_apply_id

        if self.third_part_cost_center_id is not None:
            result['third_part_cost_center_id'] = self.third_part_cost_center_id

        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id

        if self.times_total is not None:
            result['times_total'] = self.times_total

        if self.times_type is not None:
            result['times_type'] = self.times_type

        if self.times_used is not None:
            result['times_used'] = self.times_used

        if self.title is not None:
            result['title'] = self.title

        if self.traveler_standard_shrink is not None:
            result['traveler_standard'] = self.traveler_standard_shrink

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cause') is not None:
            self.cause = m.get('cause')

        if m.get('city') is not None:
            self.city = m.get('city')

        if m.get('city_code_set') is not None:
            self.city_code_set = m.get('city_code_set')

        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('finished_date') is not None:
            self.finished_date = m.get('finished_date')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_name') is not None:
            self.project_name = m.get('project_name')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('third_part_apply_id') is not None:
            self.third_part_apply_id = m.get('third_part_apply_id')

        if m.get('third_part_cost_center_id') is not None:
            self.third_part_cost_center_id = m.get('third_part_cost_center_id')

        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')

        if m.get('times_total') is not None:
            self.times_total = m.get('times_total')

        if m.get('times_type') is not None:
            self.times_type = m.get('times_type')

        if m.get('times_used') is not None:
            self.times_used = m.get('times_used')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('traveler_standard') is not None:
            self.traveler_standard_shrink = m.get('traveler_standard')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

