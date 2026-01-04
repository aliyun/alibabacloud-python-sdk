# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DistApplicationDataResponseBody(DaraModel):
    def __init__(
        self,
        dist_instance_ids: main_models.DistApplicationDataResponseBodyDistInstanceIds = None,
        dist_instance_total_count: int = None,
        dist_results: main_models.DistApplicationDataResponseBodyDistResults = None,
        request_id: str = None,
    ):
        # The list of ENS instance IDs.
        self.dist_instance_ids = dist_instance_ids
        # The total number of ENS instance IDs.
        self.dist_instance_total_count = dist_instance_total_count
        # The distribution result of the data file.
        self.dist_results = dist_results
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.dist_instance_ids:
            self.dist_instance_ids.validate()
        if self.dist_results:
            self.dist_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dist_instance_ids is not None:
            result['DistInstanceIds'] = self.dist_instance_ids.to_map()

        if self.dist_instance_total_count is not None:
            result['DistInstanceTotalCount'] = self.dist_instance_total_count

        if self.dist_results is not None:
            result['DistResults'] = self.dist_results.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistInstanceIds') is not None:
            temp_model = main_models.DistApplicationDataResponseBodyDistInstanceIds()
            self.dist_instance_ids = temp_model.from_map(m.get('DistInstanceIds'))

        if m.get('DistInstanceTotalCount') is not None:
            self.dist_instance_total_count = m.get('DistInstanceTotalCount')

        if m.get('DistResults') is not None:
            temp_model = main_models.DistApplicationDataResponseBodyDistResults()
            self.dist_results = temp_model.from_map(m.get('DistResults'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DistApplicationDataResponseBodyDistResults(DaraModel):
    def __init__(
        self,
        dist_result: List[main_models.DistApplicationDataResponseBodyDistResultsDistResult] = None,
    ):
        self.dist_result = dist_result

    def validate(self):
        if self.dist_result:
            for v1 in self.dist_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DistResult'] = []
        if self.dist_result is not None:
            for k1 in self.dist_result:
                result['DistResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dist_result = []
        if m.get('DistResult') is not None:
            for k1 in m.get('DistResult'):
                temp_model = main_models.DistApplicationDataResponseBodyDistResultsDistResult()
                self.dist_result.append(temp_model.from_map(k1))

        return self

class DistApplicationDataResponseBodyDistResultsDistResult(DaraModel):
    def __init__(
        self,
        name: str = None,
        result_code: int = None,
        result_descrip: str = None,
        version: str = None,
    ):
        # The name of the data file.
        self.name = name
        # The error code. The value is of the enumerated data type.
        self.result_code = result_code
        # The description of the distribution result.
        self.result_descrip = result_descrip
        # The version number of the data file.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_descrip is not None:
            result['ResultDescrip'] = self.result_descrip

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultDescrip') is not None:
            self.result_descrip = m.get('ResultDescrip')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DistApplicationDataResponseBodyDistInstanceIds(DaraModel):
    def __init__(
        self,
        dist_instance_id: List[str] = None,
    ):
        self.dist_instance_id = dist_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dist_instance_id is not None:
            result['DistInstanceId'] = self.dist_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistInstanceId') is not None:
            self.dist_instance_id = m.get('DistInstanceId')

        return self

