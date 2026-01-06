# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetHDMLastAliyunResourceSyncResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHDMLastAliyunResourceSyncResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

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

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetHDMLastAliyunResourceSyncResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class GetHDMLastAliyunResourceSyncResultResponseBodyData(DaraModel):
    def __init__(
        self,
        error_msg: str = None,
        results: str = None,
        sub_results: main_models.GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResults = None,
        sync_status: str = None,
    ):
        self.error_msg = error_msg
        self.results = results
        self.sub_results = sub_results
        self.sync_status = sync_status

    def validate(self):
        if self.sub_results:
            self.sub_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.results is not None:
            result['Results'] = self.results

        if self.sub_results is not None:
            result['SubResults'] = self.sub_results.to_map()

        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('Results') is not None:
            self.results = m.get('Results')

        if m.get('SubResults') is not None:
            temp_model = main_models.GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResults()
            self.sub_results = temp_model.from_map(m.get('SubResults'))

        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')

        return self

class GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResults(DaraModel):
    def __init__(
        self,
        resource_sync_sub_result: List[main_models.GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult] = None,
    ):
        self.resource_sync_sub_result = resource_sync_sub_result

    def validate(self):
        if self.resource_sync_sub_result:
            for v1 in self.resource_sync_sub_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResourceSyncSubResult'] = []
        if self.resource_sync_sub_result is not None:
            for k1 in self.resource_sync_sub_result:
                result['ResourceSyncSubResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_sync_sub_result = []
        if m.get('ResourceSyncSubResult') is not None:
            for k1 in m.get('ResourceSyncSubResult'):
                temp_model = main_models.GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult()
                self.resource_sync_sub_result.append(temp_model.from_map(k1))

        return self

class GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult(DaraModel):
    def __init__(
        self,
        err_msg: str = None,
        resource_type: str = None,
        success: bool = None,
        sync_count: int = None,
    ):
        self.err_msg = err_msg
        self.resource_type = resource_type
        self.success = success
        self.sync_count = sync_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.success is not None:
            result['Success'] = self.success

        if self.sync_count is not None:
            result['SyncCount'] = self.sync_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('SyncCount') is not None:
            self.sync_count = m.get('SyncCount')

        return self

