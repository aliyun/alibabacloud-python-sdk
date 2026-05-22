# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class BatchCreateRecordsResponseBody(DaraModel):
    def __init__(
        self,
        record_result_list: main_models.BatchCreateRecordsResponseBodyRecordResultList = None,
        request_id: str = None,
    ):
        self.record_result_list = record_result_list
        self.request_id = request_id

    def validate(self):
        if self.record_result_list:
            self.record_result_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_result_list is not None:
            result['RecordResultList'] = self.record_result_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordResultList') is not None:
            temp_model = main_models.BatchCreateRecordsResponseBodyRecordResultList()
            self.record_result_list = temp_model.from_map(m.get('RecordResultList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BatchCreateRecordsResponseBodyRecordResultList(DaraModel):
    def __init__(
        self,
        failed: List[main_models.BatchCreateRecordsResponseBodyRecordResultListFailed] = None,
        success: List[main_models.BatchCreateRecordsResponseBodyRecordResultListSuccess] = None,
        total_count: int = None,
    ):
        self.failed = failed
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.failed:
            for v1 in self.failed:
                 if v1:
                    v1.validate()
        if self.success:
            for v1 in self.success:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Failed'] = []
        if self.failed is not None:
            for k1 in self.failed:
                result['Failed'].append(k1.to_map() if k1 else None)

        result['Success'] = []
        if self.success is not None:
            for k1 in self.success:
                result['Success'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed = []
        if m.get('Failed') is not None:
            for k1 in m.get('Failed'):
                temp_model = main_models.BatchCreateRecordsResponseBodyRecordResultListFailed()
                self.failed.append(temp_model.from_map(k1))

        self.success = []
        if m.get('Success') is not None:
            for k1 in m.get('Success'):
                temp_model = main_models.BatchCreateRecordsResponseBodyRecordResultListSuccess()
                self.success.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class BatchCreateRecordsResponseBodyRecordResultListSuccess(DaraModel):
    def __init__(
        self,
        biz_name: str = None,
        data: main_models.BatchCreateRecordsResponseBodyRecordResultListSuccessData = None,
        description: str = None,
        proxied: bool = None,
        record_id: int = None,
        record_name: str = None,
        record_type: str = None,
        source_type: str = None,
        ttl: int = None,
    ):
        self.biz_name = biz_name
        self.data = data
        self.description = description
        self.proxied = proxied
        self.record_id = record_id
        self.record_name = record_name
        self.record_type = record_type
        self.source_type = source_type
        self.ttl = ttl

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.proxied is not None:
            result['Proxied'] = self.proxied

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('Data') is not None:
            temp_model = main_models.BatchCreateRecordsResponseBodyRecordResultListSuccessData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

class BatchCreateRecordsResponseBodyRecordResultListSuccessData(DaraModel):
    def __init__(
        self,
        algorithm: int = None,
        certificate: str = None,
        fingerprint: str = None,
        flag: int = None,
        key_tag: int = None,
        matching_type: int = None,
        port: int = None,
        priority: int = None,
        selector: int = None,
        tag: str = None,
        type: int = None,
        usage: int = None,
        value: str = None,
        weight: int = None,
    ):
        self.algorithm = algorithm
        self.certificate = certificate
        self.fingerprint = fingerprint
        self.flag = flag
        self.key_tag = key_tag
        self.matching_type = matching_type
        self.port = port
        self.priority = priority
        self.selector = selector
        self.tag = tag
        self.type = type
        self.usage = usage
        self.value = value
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint

        if self.flag is not None:
            result['Flag'] = self.flag

        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag

        if self.matching_type is not None:
            result['MatchingType'] = self.matching_type

        if self.port is not None:
            result['Port'] = self.port

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.selector is not None:
            result['Selector'] = self.selector

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.type is not None:
            result['Type'] = self.type

        if self.usage is not None:
            result['Usage'] = self.usage

        if self.value is not None:
            result['Value'] = self.value

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        if m.get('Flag') is not None:
            self.flag = m.get('Flag')

        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')

        if m.get('MatchingType') is not None:
            self.matching_type = m.get('MatchingType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Selector') is not None:
            self.selector = m.get('Selector')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class BatchCreateRecordsResponseBodyRecordResultListFailed(DaraModel):
    def __init__(
        self,
        biz_name: str = None,
        data: main_models.BatchCreateRecordsResponseBodyRecordResultListFailedData = None,
        description: str = None,
        proxied: bool = None,
        record_id: int = None,
        record_name: str = None,
        record_type: str = None,
        source_type: str = None,
        ttl: int = None,
    ):
        self.biz_name = biz_name
        self.data = data
        self.description = description
        self.proxied = proxied
        self.record_id = record_id
        self.record_name = record_name
        self.record_type = record_type
        self.source_type = source_type
        self.ttl = ttl

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.proxied is not None:
            result['Proxied'] = self.proxied

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('Data') is not None:
            temp_model = main_models.BatchCreateRecordsResponseBodyRecordResultListFailedData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

class BatchCreateRecordsResponseBodyRecordResultListFailedData(DaraModel):
    def __init__(
        self,
        algorithm: int = None,
        certificate: str = None,
        fingerprint: str = None,
        flag: int = None,
        key_tag: int = None,
        matching_type: int = None,
        port: int = None,
        priority: int = None,
        selector: int = None,
        tag: str = None,
        type: int = None,
        usage: int = None,
        value: str = None,
        weight: int = None,
    ):
        self.algorithm = algorithm
        self.certificate = certificate
        self.fingerprint = fingerprint
        self.flag = flag
        self.key_tag = key_tag
        self.matching_type = matching_type
        self.port = port
        self.priority = priority
        self.selector = selector
        self.tag = tag
        self.type = type
        self.usage = usage
        self.value = value
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint

        if self.flag is not None:
            result['Flag'] = self.flag

        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag

        if self.matching_type is not None:
            result['MatchingType'] = self.matching_type

        if self.port is not None:
            result['Port'] = self.port

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.selector is not None:
            result['Selector'] = self.selector

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.type is not None:
            result['Type'] = self.type

        if self.usage is not None:
            result['Usage'] = self.usage

        if self.value is not None:
            result['Value'] = self.value

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        if m.get('Flag') is not None:
            self.flag = m.get('Flag')

        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')

        if m.get('MatchingType') is not None:
            self.matching_type = m.get('MatchingType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Selector') is not None:
            self.selector = m.get('Selector')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

