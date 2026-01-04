# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeGrantRulesToEcrResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        ecr_grant_rules: List[main_models.DescribeGrantRulesToEcrResponseBodyEcrGrantRules] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The total number of entries returned.
        self.count = count
        # The cross-account authorization list of the ECR
        self.ecr_grant_rules = ecr_grant_rules
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries on each page. Maximum value: 50. Default value: 10.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ecr_grant_rules:
            for v1 in self.ecr_grant_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['EcrGrantRules'] = []
        if self.ecr_grant_rules is not None:
            for k1 in self.ecr_grant_rules:
                result['EcrGrantRules'].append(k1.to_map() if k1 else None)

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
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.ecr_grant_rules = []
        if m.get('EcrGrantRules') is not None:
            for k1 in m.get('EcrGrantRules'):
                temp_model = main_models.DescribeGrantRulesToEcrResponseBodyEcrGrantRules()
                self.ecr_grant_rules.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeGrantRulesToEcrResponseBodyEcrGrantRules(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        ecr_instance_id: str = None,
        ecr_uid: int = None,
    ):
        # The authorization time. The time follows the ISO8601 standard and uses UTC time. The format is YYYY-MM-DDThh:mm:ssZ.
        self.create_time = create_time
        # The ECR account ID.
        self.ecr_instance_id = ecr_instance_id
        # The ECR account ID.
        self.ecr_uid = ecr_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.ecr_instance_id is not None:
            result['EcrInstanceId'] = self.ecr_instance_id

        if self.ecr_uid is not None:
            result['EcrUid'] = self.ecr_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EcrInstanceId') is not None:
            self.ecr_instance_id = m.get('EcrInstanceId')

        if m.get('EcrUid') is not None:
            self.ecr_uid = m.get('EcrUid')

        return self

