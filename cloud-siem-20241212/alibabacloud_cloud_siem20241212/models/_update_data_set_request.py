# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class UpdateDataSetRequest(DaraModel):
    def __init__(
        self,
        data_set_description: str = None,
        data_set_file_name: str = None,
        data_set_id: str = None,
        data_set_name: str = None,
        data_set_status: int = None,
        ip_whitelist_recognizers: List[main_models.UpdateDataSetRequestIpWhitelistRecognizers] = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_set_description = data_set_description
        self.data_set_file_name = data_set_file_name
        # This parameter is required.
        self.data_set_id = data_set_id
        self.data_set_name = data_set_name
        self.data_set_status = data_set_status
        self.ip_whitelist_recognizers = ip_whitelist_recognizers
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        if self.ip_whitelist_recognizers:
            for v1 in self.ip_whitelist_recognizers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_set_description is not None:
            result['DataSetDescription'] = self.data_set_description

        if self.data_set_file_name is not None:
            result['DataSetFileName'] = self.data_set_file_name

        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id

        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name

        if self.data_set_status is not None:
            result['DataSetStatus'] = self.data_set_status

        result['IpWhitelistRecognizers'] = []
        if self.ip_whitelist_recognizers is not None:
            for k1 in self.ip_whitelist_recognizers:
                result['IpWhitelistRecognizers'].append(k1.to_map() if k1 else None)

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetDescription') is not None:
            self.data_set_description = m.get('DataSetDescription')

        if m.get('DataSetFileName') is not None:
            self.data_set_file_name = m.get('DataSetFileName')

        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')

        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')

        if m.get('DataSetStatus') is not None:
            self.data_set_status = m.get('DataSetStatus')

        self.ip_whitelist_recognizers = []
        if m.get('IpWhitelistRecognizers') is not None:
            for k1 in m.get('IpWhitelistRecognizers'):
                temp_model = main_models.UpdateDataSetRequestIpWhitelistRecognizers()
                self.ip_whitelist_recognizers.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

class UpdateDataSetRequestIpWhitelistRecognizers(DaraModel):
    def __init__(
        self,
        auto_recognize_status: str = None,
        ip_whitelist_recognizer_type: str = None,
        recognize_scope: str = None,
    ):
        self.auto_recognize_status = auto_recognize_status
        self.ip_whitelist_recognizer_type = ip_whitelist_recognizer_type
        self.recognize_scope = recognize_scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_recognize_status is not None:
            result['AutoRecognizeStatus'] = self.auto_recognize_status

        if self.ip_whitelist_recognizer_type is not None:
            result['IpWhitelistRecognizerType'] = self.ip_whitelist_recognizer_type

        if self.recognize_scope is not None:
            result['RecognizeScope'] = self.recognize_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRecognizeStatus') is not None:
            self.auto_recognize_status = m.get('AutoRecognizeStatus')

        if m.get('IpWhitelistRecognizerType') is not None:
            self.ip_whitelist_recognizer_type = m.get('IpWhitelistRecognizerType')

        if m.get('RecognizeScope') is not None:
            self.recognize_scope = m.get('RecognizeScope')

        return self

