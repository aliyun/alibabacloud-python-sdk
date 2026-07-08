# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchBindTemplatesRequest(DaraModel):
    def __init__(
        self,
        apply_all: bool = None,
        instance_id: str = None,
        instance_type: str = None,
        owner_id: int = None,
        replace: bool = None,
        template_id: str = None,
        template_type: str = None,
    ):
        # Specifies whether to apply the template to all streams in the scope. The default value is false.
        self.apply_all = apply_all
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The instance type. Valid values:
        # 
        # - group
        # 
        # - stream
        # 
        # This parameter is required.
        self.instance_type = instance_type
        self.owner_id = owner_id
        # Specifies whether to replace existing bindings. The default value is false.
        self.replace = replace
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The template type. Valid values:
        # 
        # - record (recording)
        # 
        # - snapshot (snapshotting)
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_all is not None:
            result['ApplyAll'] = self.apply_all

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.replace is not None:
            result['Replace'] = self.replace

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyAll') is not None:
            self.apply_all = m.get('ApplyAll')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Replace') is not None:
            self.replace = m.get('Replace')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

