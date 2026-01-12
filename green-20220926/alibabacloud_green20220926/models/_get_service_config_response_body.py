# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetServiceConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetServiceConfigResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code.
        self.code = code
        # Returned data.
        self.data = data
        # Further description of the error code.
        self.msg = msg
        # Request ID.
        self.request_id = request_id
        # Success indicator.
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

        if self.msg is not None:
            result['Msg'] = self.msg

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
            temp_model = main_models.GetServiceConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetServiceConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        custom_service_conf: main_models.GetServiceConfigResponseBodyDataCustomServiceConf = None,
        gmt_modified: str = None,
        resource_type: str = None,
        service_code: str = None,
        uid: str = None,
    ):
        # Custom service details
        self.custom_service_conf = custom_service_conf
        # Modification time.
        self.gmt_modified = gmt_modified
        # Resource type.
        self.resource_type = resource_type
        # Service code.
        self.service_code = service_code
        # UID.
        self.uid = uid

    def validate(self):
        if self.custom_service_conf:
            self.custom_service_conf.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_service_conf is not None:
            result['CustomServiceConf'] = self.custom_service_conf.to_map()

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomServiceConf') is not None:
            temp_model = main_models.GetServiceConfigResponseBodyDataCustomServiceConf()
            self.custom_service_conf = temp_model.from_map(m.get('CustomServiceConf'))

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

class GetServiceConfigResponseBodyDataCustomServiceConf(DaraModel):
    def __init__(
        self,
        keyword_filter_libs: List[str] = None,
        keyword_hit_libs: List[str] = None,
        manual_machine_config: main_models.GetServiceConfigResponseBodyDataCustomServiceConfManualMachineConfig = None,
        similar_text_hit_libs: List[str] = None,
    ):
        # Ignore word libraries.
        self.keyword_filter_libs = keyword_filter_libs
        # Hit word libraries.
        self.keyword_hit_libs = keyword_hit_libs
        # Human-machine review configuration.
        self.manual_machine_config = manual_machine_config
        # Hit similar text libraries.
        self.similar_text_hit_libs = similar_text_hit_libs

    def validate(self):
        if self.manual_machine_config:
            self.manual_machine_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword_filter_libs is not None:
            result['KeywordFilterLibs'] = self.keyword_filter_libs

        if self.keyword_hit_libs is not None:
            result['KeywordHitLibs'] = self.keyword_hit_libs

        if self.manual_machine_config is not None:
            result['ManualMachineConfig'] = self.manual_machine_config.to_map()

        if self.similar_text_hit_libs is not None:
            result['SimilarTextHitLibs'] = self.similar_text_hit_libs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeywordFilterLibs') is not None:
            self.keyword_filter_libs = m.get('KeywordFilterLibs')

        if m.get('KeywordHitLibs') is not None:
            self.keyword_hit_libs = m.get('KeywordHitLibs')

        if m.get('ManualMachineConfig') is not None:
            temp_model = main_models.GetServiceConfigResponseBodyDataCustomServiceConfManualMachineConfig()
            self.manual_machine_config = temp_model.from_map(m.get('ManualMachineConfig'))

        if m.get('SimilarTextHitLibs') is not None:
            self.similar_text_hit_libs = m.get('SimilarTextHitLibs')

        return self

class GetServiceConfigResponseBodyDataCustomServiceConfManualMachineConfig(DaraModel):
    def __init__(
        self,
        audit_risk_levels: List[str] = None,
        callback_id: int = None,
        enable: bool = None,
        manual_service: str = None,
    ):
        # Risk levels.
        self.audit_risk_levels = audit_risk_levels
        # Callback notification ID
        self.callback_id = callback_id
        # Whether to enable. Values:
        # - **true**: Enabled
        # - **false**: Disabled
        self.enable = enable
        # Manual review service
        self.manual_service = manual_service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_risk_levels is not None:
            result['AuditRiskLevels'] = self.audit_risk_levels

        if self.callback_id is not None:
            result['CallbackId'] = self.callback_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.manual_service is not None:
            result['ManualService'] = self.manual_service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditRiskLevels') is not None:
            self.audit_risk_levels = m.get('AuditRiskLevels')

        if m.get('CallbackId') is not None:
            self.callback_id = m.get('CallbackId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('ManualService') is not None:
            self.manual_service = m.get('ManualService')

        return self

