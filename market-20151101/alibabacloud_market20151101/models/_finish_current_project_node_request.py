# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FinishCurrentProjectNodeRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        node_id: int = None,
        remark: str = None,
        template_form: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.node_id = node_id
        self.remark = remark
        self.template_form = template_form

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.template_form is not None:
            result['TemplateForm'] = self.template_form

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('TemplateForm') is not None:
            self.template_form = m.get('TemplateForm')

        return self

