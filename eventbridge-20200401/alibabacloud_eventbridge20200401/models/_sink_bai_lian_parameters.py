# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class SinkBaiLianParameters(DaraModel):
    def __init__(
        self,
        after: main_models.SinkBaiLianParametersAfter = None,
        application_type: str = None,
        before: main_models.SinkBaiLianParametersBefore = None,
        context: Any = None,
        extend: Any = None,
        offset: main_models.SinkBaiLianParametersOffset = None,
        op: main_models.SinkBaiLianParametersOp = None,
        partition: main_models.SinkBaiLianParametersPartition = None,
        workspace_id: str = None,
    ):
        self.after = after
        self.application_type = application_type
        self.before = before
        self.context = context
        self.extend = extend
        self.offset = offset
        self.op = op
        self.partition = partition
        self.workspace_id = workspace_id

    def validate(self):
        if self.after:
            self.after.validate()
        if self.before:
            self.before.validate()
        if self.offset:
            self.offset.validate()
        if self.op:
            self.op.validate()
        if self.partition:
            self.partition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after is not None:
            result['After'] = self.after.to_map()

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.before is not None:
            result['Before'] = self.before.to_map()

        if self.context is not None:
            result['Context'] = self.context

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.offset is not None:
            result['Offset'] = self.offset.to_map()

        if self.op is not None:
            result['Op'] = self.op.to_map()

        if self.partition is not None:
            result['Partition'] = self.partition.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('After') is not None:
            temp_model = main_models.SinkBaiLianParametersAfter()
            self.after = temp_model.from_map(m.get('After'))

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('Before') is not None:
            temp_model = main_models.SinkBaiLianParametersBefore()
            self.before = temp_model.from_map(m.get('Before'))

        if m.get('Context') is not None:
            self.context = m.get('Context')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('Offset') is not None:
            temp_model = main_models.SinkBaiLianParametersOffset()
            self.offset = temp_model.from_map(m.get('Offset'))

        if m.get('Op') is not None:
            temp_model = main_models.SinkBaiLianParametersOp()
            self.op = temp_model.from_map(m.get('Op'))

        if m.get('Partition') is not None:
            temp_model = main_models.SinkBaiLianParametersPartition()
            self.partition = temp_model.from_map(m.get('Partition'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class SinkBaiLianParametersPartition(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SinkBaiLianParametersOp(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SinkBaiLianParametersOffset(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SinkBaiLianParametersBefore(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SinkBaiLianParametersAfter(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

