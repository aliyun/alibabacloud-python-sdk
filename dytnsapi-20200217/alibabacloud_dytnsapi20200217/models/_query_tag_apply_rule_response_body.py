# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class QueryTagApplyRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryTagApplyRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The request status code. **OK** indicates success.
        self.code = code
        # The returned data.
        self.data = data
        # The description of the returned status code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - true: successful.
        # 
        # - false: failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryTagApplyRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryTagApplyRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        apply_material_desc: str = None,
        auto_audit: int = None,
        charging_standard_link: str = None,
        encrypted_query: int = None,
        need_apply_material: int = None,
        sla_link: str = None,
    ):
        # The application material requirements. This parameter is returned when NeedApplyMaterial=1.
        self.apply_material_desc = apply_material_desc
        # Indicates whether to automatically approve. Valid values:
        # 
        # - 0: do not automatically approve.
        # 
        # - 1: automatically approve.
        self.auto_audit = auto_audit
        # The billing standard description link.
        self.charging_standard_link = charging_standard_link
        # Indicates whether encrypted query is supported. Valid values:
        # 
        # - 0: not supported.
        # 
        # - 1: supported.
        self.encrypted_query = encrypted_query
        # Indicates whether application materials need to be provided. Valid values:
        # 
        # - 0: not required.
        # 
        # - 1: required.
        self.need_apply_material = need_apply_material
        # The service agreement link.
        self.sla_link = sla_link

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_material_desc is not None:
            result['ApplyMaterialDesc'] = self.apply_material_desc

        if self.auto_audit is not None:
            result['AutoAudit'] = self.auto_audit

        if self.charging_standard_link is not None:
            result['ChargingStandardLink'] = self.charging_standard_link

        if self.encrypted_query is not None:
            result['EncryptedQuery'] = self.encrypted_query

        if self.need_apply_material is not None:
            result['NeedApplyMaterial'] = self.need_apply_material

        if self.sla_link is not None:
            result['SlaLink'] = self.sla_link

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyMaterialDesc') is not None:
            self.apply_material_desc = m.get('ApplyMaterialDesc')

        if m.get('AutoAudit') is not None:
            self.auto_audit = m.get('AutoAudit')

        if m.get('ChargingStandardLink') is not None:
            self.charging_standard_link = m.get('ChargingStandardLink')

        if m.get('EncryptedQuery') is not None:
            self.encrypted_query = m.get('EncryptedQuery')

        if m.get('NeedApplyMaterial') is not None:
            self.need_apply_material = m.get('NeedApplyMaterial')

        if m.get('SlaLink') is not None:
            self.sla_link = m.get('SlaLink')

        return self

