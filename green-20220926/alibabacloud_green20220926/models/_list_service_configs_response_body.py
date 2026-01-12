# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class ListServiceConfigsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListServiceConfigsResponseBodyData] = None,
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
        # ID assigned by the backend to uniquely identify a request. Can be used for troubleshooting.
        self.request_id = request_id
        # Success indicator.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListServiceConfigsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListServiceConfigsResponseBodyData(DaraModel):
    def __init__(
        self,
        classify: str = None,
        copy_from: str = None,
        custom_service_conf: main_models.ListServiceConfigsResponseBodyDataCustomServiceConf = None,
        gmt_modified: str = None,
        option: Dict[str, Any] = None,
        resource_type: str = None,
        service_code: str = None,
        service_desc: str = None,
        service_name: str = None,
        service_type: str = None,
        uid: str = None,
        use_status: str = None,
    ):
        # Category.
        self.classify = classify
        # Main service.
        self.copy_from = copy_from
        # Service configuration.
        self.custom_service_conf = custom_service_conf
        # Modification time.
        self.gmt_modified = gmt_modified
        # Options.
        self.option = option
        # Resource type.
        self.resource_type = resource_type
        # Service code.
        self.service_code = service_code
        # Service description.
        self.service_desc = service_desc
        # Service name.
        self.service_name = service_name
        # Service type.
        self.service_type = service_type
        # UID.
        self.uid = uid
        # Usage status
        self.use_status = use_status

    def validate(self):
        if self.custom_service_conf:
            self.custom_service_conf.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classify is not None:
            result['Classify'] = self.classify

        if self.copy_from is not None:
            result['CopyFrom'] = self.copy_from

        if self.custom_service_conf is not None:
            result['CustomServiceConf'] = self.custom_service_conf.to_map()

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.option is not None:
            result['Option'] = self.option

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.service_desc is not None:
            result['ServiceDesc'] = self.service_desc

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.use_status is not None:
            result['UseStatus'] = self.use_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        if m.get('CopyFrom') is not None:
            self.copy_from = m.get('CopyFrom')

        if m.get('CustomServiceConf') is not None:
            temp_model = main_models.ListServiceConfigsResponseBodyDataCustomServiceConf()
            self.custom_service_conf = temp_model.from_map(m.get('CustomServiceConf'))

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('ServiceDesc') is not None:
            self.service_desc = m.get('ServiceDesc')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UseStatus') is not None:
            self.use_status = m.get('UseStatus')

        return self

class ListServiceConfigsResponseBodyDataCustomServiceConf(DaraModel):
    def __init__(
        self,
        audio_service: str = None,
        image_service: List[str] = None,
        keyword_filter_libs: List[str] = None,
        keyword_hit_libs: List[str] = None,
        rules: List[main_models.ListServiceConfigsResponseBodyDataCustomServiceConfRules] = None,
        similar_text_hit_libs: List[str] = None,
    ):
        # Audio service.
        self.audio_service = audio_service
        # Image services.
        self.image_service = image_service
        # Ignored word libraries.
        self.keyword_filter_libs = keyword_filter_libs
        # Hit word libraries.
        self.keyword_hit_libs = keyword_hit_libs
        # Service rules
        self.rules = rules
        # Hit similar text libraries.
        self.similar_text_hit_libs = similar_text_hit_libs

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_service is not None:
            result['AudioService'] = self.audio_service

        if self.image_service is not None:
            result['ImageService'] = self.image_service

        if self.keyword_filter_libs is not None:
            result['KeywordFilterLibs'] = self.keyword_filter_libs

        if self.keyword_hit_libs is not None:
            result['KeywordHitLibs'] = self.keyword_hit_libs

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.similar_text_hit_libs is not None:
            result['SimilarTextHitLibs'] = self.similar_text_hit_libs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioService') is not None:
            self.audio_service = m.get('AudioService')

        if m.get('ImageService') is not None:
            self.image_service = m.get('ImageService')

        if m.get('KeywordFilterLibs') is not None:
            self.keyword_filter_libs = m.get('KeywordFilterLibs')

        if m.get('KeywordHitLibs') is not None:
            self.keyword_hit_libs = m.get('KeywordHitLibs')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ListServiceConfigsResponseBodyDataCustomServiceConfRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('SimilarTextHitLibs') is not None:
            self.similar_text_hit_libs = m.get('SimilarTextHitLibs')

        return self

class ListServiceConfigsResponseBodyDataCustomServiceConfRules(DaraModel):
    def __init__(
        self,
        image_scan_rule: main_models.ListServiceConfigsResponseBodyDataCustomServiceConfRulesImageScanRule = None,
        index: int = None,
        text_scan_rule: main_models.ListServiceConfigsResponseBodyDataCustomServiceConfRulesTextScanRule = None,
    ):
        # Image review rule.
        self.image_scan_rule = image_scan_rule
        # Index.
        self.index = index
        # Text review rule.
        self.text_scan_rule = text_scan_rule

    def validate(self):
        if self.image_scan_rule:
            self.image_scan_rule.validate()
        if self.text_scan_rule:
            self.text_scan_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_scan_rule is not None:
            result['ImageScanRule'] = self.image_scan_rule.to_map()

        if self.index is not None:
            result['Index'] = self.index

        if self.text_scan_rule is not None:
            result['TextScanRule'] = self.text_scan_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageScanRule') is not None:
            temp_model = main_models.ListServiceConfigsResponseBodyDataCustomServiceConfRulesImageScanRule()
            self.image_scan_rule = temp_model.from_map(m.get('ImageScanRule'))

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('TextScanRule') is not None:
            temp_model = main_models.ListServiceConfigsResponseBodyDataCustomServiceConfRulesTextScanRule()
            self.text_scan_rule = temp_model.from_map(m.get('TextScanRule'))

        return self

class ListServiceConfigsResponseBodyDataCustomServiceConfRulesTextScanRule(DaraModel):
    def __init__(
        self,
        services: List[str] = None,
    ):
        # Text services.
        self.services = services

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.services is not None:
            result['Services'] = self.services

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Services') is not None:
            self.services = m.get('Services')

        return self

class ListServiceConfigsResponseBodyDataCustomServiceConfRulesImageScanRule(DaraModel):
    def __init__(
        self,
        services: List[str] = None,
    ):
        # Image services.
        self.services = services

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.services is not None:
            result['Services'] = self.services

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Services') is not None:
            self.services = m.get('Services')

        return self

