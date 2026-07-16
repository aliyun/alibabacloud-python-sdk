# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aideepsign20260511 import models as main_models
from darabonba.model import DaraModel

class GetSensitiveScanResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetSensitiveScanResultResponseBodyResult = None,
        status: str = None,
        success: bool = None,
    ):
        # The business error code. The value "OK" is returned when the request succeeds.
        self.code = code
        # The HTTP status code. The value 200 is returned when the request succeeds.
        self.http_status_code = http_status_code
        # The additional information. The value "success" is returned when the request succeeds.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The scan result. This parameter is returned only when the status is completed.
        self.result = result
        # The task status. Valid values:
        # - running: The task is running.
        # - completed: The task is completed.
        # - terminated: The task is terminated or failed.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetSensitiveScanResultResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSensitiveScanResultResponseBodyResult(DaraModel):
    def __init__(
        self,
        oss_object_detail: main_models.GetSensitiveScanResultResponseBodyResultOssObjectDetail = None,
    ):
        # The name of the scanned object.
        self.oss_object_detail = oss_object_detail

    def validate(self):
        if self.oss_object_detail:
            self.oss_object_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_object_detail is not None:
            result['OssObjectDetail'] = self.oss_object_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssObjectDetail') is not None:
            temp_model = main_models.GetSensitiveScanResultResponseBodyResultOssObjectDetail()
            self.oss_object_detail = temp_model.from_map(m.get('OssObjectDetail'))

        return self

class GetSensitiveScanResultResponseBodyResultOssObjectDetail(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        category_name: str = None,
        name: str = None,
        risk_level_name: str = None,
        rule_list: List[main_models.GetSensitiveScanResultResponseBodyResultOssObjectDetailRuleList] = None,
    ):
        # The name of the bucket to which the object belongs.
        self.bucket_name = bucket_name
        # The sensitive data category name.
        self.category_name = category_name
        # The name of the scanned object.
        self.name = name
        # The overall risk level name.
        self.risk_level_name = risk_level_name
        # The list of sensitive data rules that are hit.
        self.rule_list = rule_list

    def validate(self):
        if self.rule_list:
            for v1 in self.rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.name is not None:
            result['Name'] = self.name

        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name

        result['RuleList'] = []
        if self.rule_list is not None:
            for k1 in self.rule_list:
                result['RuleList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')

        self.rule_list = []
        if m.get('RuleList') is not None:
            for k1 in m.get('RuleList'):
                temp_model = main_models.GetSensitiveScanResultResponseBodyResultOssObjectDetailRuleList()
                self.rule_list.append(temp_model.from_map(k1))

        return self

class GetSensitiveScanResultResponseBodyResultOssObjectDetailRuleList(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        count: int = None,
        risk_level_name: str = None,
        rule_name: str = None,
    ):
        # The category name of the rule.
        self.category_name = category_name
        # The number of hits.
        self.count = count
        # The risk level name of the rule.
        self.risk_level_name = risk_level_name
        # The rule name.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.count is not None:
            result['Count'] = self.count

        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

