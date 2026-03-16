# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class InitTenantAliasResponseBody(DaraModel):
    def __init__(
        self,
        alias_info: main_models.InitTenantAliasResponseBodyAliasInfo = None,
        data: str = None,
        request_id: str = None,
    ):
        # The data returned.
        self.alias_info = alias_info
        # The generated ID of the organization.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.alias_info:
            self.alias_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_info is not None:
            result['AliasInfo'] = self.alias_info.to_map()

        if self.data is not None:
            result['Data'] = self.data

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasInfo') is not None:
            temp_model = main_models.InitTenantAliasResponseBodyAliasInfo()
            self.alias_info = temp_model.from_map(m.get('AliasInfo'))

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class InitTenantAliasResponseBodyAliasInfo(DaraModel):
    def __init__(
        self,
        alias_edit_disabled_reason: str = None,
        alias_editable: bool = None,
        alias_source_type: str = None,
        next_modify_time: str = None,
    ):
        # The reason why modification is not allowed.
        self.alias_edit_disabled_reason = alias_edit_disabled_reason
        # Indicates whether modification is allowed.
        self.alias_editable = alias_editable
        # The source of the organization ID.
        # 
        # Valid values:
        # 
        # *   Generated: auto-generated.
        # *   Customized: user-defined.
        self.alias_source_type = alias_source_type
        # The time window during which modification is allowed.
        self.next_modify_time = next_modify_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_edit_disabled_reason is not None:
            result['AliasEditDisabledReason'] = self.alias_edit_disabled_reason

        if self.alias_editable is not None:
            result['AliasEditable'] = self.alias_editable

        if self.alias_source_type is not None:
            result['AliasSourceType'] = self.alias_source_type

        if self.next_modify_time is not None:
            result['NextModifyTime'] = self.next_modify_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasEditDisabledReason') is not None:
            self.alias_edit_disabled_reason = m.get('AliasEditDisabledReason')

        if m.get('AliasEditable') is not None:
            self.alias_editable = m.get('AliasEditable')

        if m.get('AliasSourceType') is not None:
            self.alias_source_type = m.get('AliasSourceType')

        if m.get('NextModifyTime') is not None:
            self.next_modify_time = m.get('NextModifyTime')

        return self

