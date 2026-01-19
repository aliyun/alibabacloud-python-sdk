# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeUpdateVpcInfoTaskResponseBody(DaraModel):
    def __init__(
        self,
        api_update_vpc_info_results: main_models.DescribeUpdateVpcInfoTaskResponseBodyApiUpdateVpcInfoResults = None,
        request_id: str = None,
    ):
        self.api_update_vpc_info_results = api_update_vpc_info_results
        self.request_id = request_id

    def validate(self):
        if self.api_update_vpc_info_results:
            self.api_update_vpc_info_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_update_vpc_info_results is not None:
            result['ApiUpdateVpcInfoResults'] = self.api_update_vpc_info_results.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiUpdateVpcInfoResults') is not None:
            temp_model = main_models.DescribeUpdateVpcInfoTaskResponseBodyApiUpdateVpcInfoResults()
            self.api_update_vpc_info_results = temp_model.from_map(m.get('ApiUpdateVpcInfoResults'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUpdateVpcInfoTaskResponseBodyApiUpdateVpcInfoResults(DaraModel):
    def __init__(
        self,
        api_update_vpc_info_result: List[main_models.DescribeUpdateVpcInfoTaskResponseBodyApiUpdateVpcInfoResultsApiUpdateVpcInfoResult] = None,
    ):
        self.api_update_vpc_info_result = api_update_vpc_info_result

    def validate(self):
        if self.api_update_vpc_info_result:
            for v1 in self.api_update_vpc_info_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiUpdateVpcInfoResult'] = []
        if self.api_update_vpc_info_result is not None:
            for k1 in self.api_update_vpc_info_result:
                result['ApiUpdateVpcInfoResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_update_vpc_info_result = []
        if m.get('ApiUpdateVpcInfoResult') is not None:
            for k1 in m.get('ApiUpdateVpcInfoResult'):
                temp_model = main_models.DescribeUpdateVpcInfoTaskResponseBodyApiUpdateVpcInfoResultsApiUpdateVpcInfoResult()
                self.api_update_vpc_info_result.append(temp_model.from_map(k1))

        return self

class DescribeUpdateVpcInfoTaskResponseBodyApiUpdateVpcInfoResultsApiUpdateVpcInfoResult(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        api_uid: str = None,
        error_msg: str = None,
        group_id: str = None,
        group_name: str = None,
        stage_id: str = None,
        stage_name: str = None,
        update_status: str = None,
    ):
        self.api_name = api_name
        self.api_uid = api_uid
        self.error_msg = error_msg
        self.group_id = group_id
        self.group_name = group_name
        self.stage_id = stage_id
        self.stage_name = stage_name
        self.update_status = update_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.update_status is not None:
            result['UpdateStatus'] = self.update_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('UpdateStatus') is not None:
            self.update_status = m.get('UpdateStatus')

        return self

