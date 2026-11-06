# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListDataSetsResponseBody(DaraModel):
    def __init__(
        self,
        data_sets: List[main_models.ListDataSetsResponseBodyDataSets] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data_sets = data_sets
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data_sets:
            for v1 in self.data_sets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataSets'] = []
        if self.data_sets is not None:
            for k1 in self.data_sets:
                result['DataSets'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_sets = []
        if m.get('DataSets') is not None:
            for k1 in m.get('DataSets'):
                temp_model = main_models.ListDataSetsResponseBodyDataSets()
                self.data_sets.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataSetsResponseBodyDataSets(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        data_set_description: str = None,
        data_set_field_key_name: str = None,
        data_set_field_names: str = None,
        data_set_file_name: str = None,
        data_set_id: str = None,
        data_set_name: str = None,
        data_set_references: List[main_models.ListDataSetsResponseBodyDataSetsDataSetReferences] = None,
        data_set_status: int = None,
        data_set_type: str = None,
        ip_whitelist_recognizers: List[main_models.ListDataSetsResponseBodyDataSetsIpWhitelistRecognizers] = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.data_set_description = data_set_description
        self.data_set_field_key_name = data_set_field_key_name
        self.data_set_field_names = data_set_field_names
        self.data_set_file_name = data_set_file_name
        self.data_set_id = data_set_id
        self.data_set_name = data_set_name
        self.data_set_references = data_set_references
        self.data_set_status = data_set_status
        self.data_set_type = data_set_type
        self.ip_whitelist_recognizers = ip_whitelist_recognizers
        self.update_time = update_time

    def validate(self):
        if self.data_set_references:
            for v1 in self.data_set_references:
                 if v1:
                    v1.validate()
        if self.ip_whitelist_recognizers:
            for v1 in self.ip_whitelist_recognizers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_set_description is not None:
            result['DataSetDescription'] = self.data_set_description

        if self.data_set_field_key_name is not None:
            result['DataSetFieldKeyName'] = self.data_set_field_key_name

        if self.data_set_field_names is not None:
            result['DataSetFieldNames'] = self.data_set_field_names

        if self.data_set_file_name is not None:
            result['DataSetFileName'] = self.data_set_file_name

        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id

        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name

        result['DataSetReferences'] = []
        if self.data_set_references is not None:
            for k1 in self.data_set_references:
                result['DataSetReferences'].append(k1.to_map() if k1 else None)

        if self.data_set_status is not None:
            result['DataSetStatus'] = self.data_set_status

        if self.data_set_type is not None:
            result['DataSetType'] = self.data_set_type

        result['IpWhitelistRecognizers'] = []
        if self.ip_whitelist_recognizers is not None:
            for k1 in self.ip_whitelist_recognizers:
                result['IpWhitelistRecognizers'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSetDescription') is not None:
            self.data_set_description = m.get('DataSetDescription')

        if m.get('DataSetFieldKeyName') is not None:
            self.data_set_field_key_name = m.get('DataSetFieldKeyName')

        if m.get('DataSetFieldNames') is not None:
            self.data_set_field_names = m.get('DataSetFieldNames')

        if m.get('DataSetFileName') is not None:
            self.data_set_file_name = m.get('DataSetFileName')

        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')

        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')

        self.data_set_references = []
        if m.get('DataSetReferences') is not None:
            for k1 in m.get('DataSetReferences'):
                temp_model = main_models.ListDataSetsResponseBodyDataSetsDataSetReferences()
                self.data_set_references.append(temp_model.from_map(k1))

        if m.get('DataSetStatus') is not None:
            self.data_set_status = m.get('DataSetStatus')

        if m.get('DataSetType') is not None:
            self.data_set_type = m.get('DataSetType')

        self.ip_whitelist_recognizers = []
        if m.get('IpWhitelistRecognizers') is not None:
            for k1 in m.get('IpWhitelistRecognizers'):
                temp_model = main_models.ListDataSetsResponseBodyDataSetsIpWhitelistRecognizers()
                self.ip_whitelist_recognizers.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListDataSetsResponseBodyDataSetsIpWhitelistRecognizers(DaraModel):
    def __init__(
        self,
        auto_recognize_status: str = None,
        ip_whitelist_recognizer_type: str = None,
        recognize_scope: str = None,
        update_time: int = None,
    ):
        self.auto_recognize_status = auto_recognize_status
        self.ip_whitelist_recognizer_type = ip_whitelist_recognizer_type
        self.recognize_scope = recognize_scope
        self.update_time = update_time

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

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRecognizeStatus') is not None:
            self.auto_recognize_status = m.get('AutoRecognizeStatus')

        if m.get('IpWhitelistRecognizerType') is not None:
            self.ip_whitelist_recognizer_type = m.get('IpWhitelistRecognizerType')

        if m.get('RecognizeScope') is not None:
            self.recognize_scope = m.get('RecognizeScope')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListDataSetsResponseBodyDataSetsDataSetReferences(DaraModel):
    def __init__(
        self,
        data_set_id: str = None,
        data_set_reference_id: str = None,
        data_set_reference_name: str = None,
        data_set_reference_type: str = None,
    ):
        self.data_set_id = data_set_id
        self.data_set_reference_id = data_set_reference_id
        self.data_set_reference_name = data_set_reference_name
        self.data_set_reference_type = data_set_reference_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id

        if self.data_set_reference_id is not None:
            result['DataSetReferenceId'] = self.data_set_reference_id

        if self.data_set_reference_name is not None:
            result['DataSetReferenceName'] = self.data_set_reference_name

        if self.data_set_reference_type is not None:
            result['DataSetReferenceType'] = self.data_set_reference_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')

        if m.get('DataSetReferenceId') is not None:
            self.data_set_reference_id = m.get('DataSetReferenceId')

        if m.get('DataSetReferenceName') is not None:
            self.data_set_reference_name = m.get('DataSetReferenceName')

        if m.get('DataSetReferenceType') is not None:
            self.data_set_reference_type = m.get('DataSetReferenceType')

        return self

