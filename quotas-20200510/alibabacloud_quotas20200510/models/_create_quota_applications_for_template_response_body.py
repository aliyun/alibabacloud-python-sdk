# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class CreateQuotaApplicationsForTemplateResponseBody(DaraModel):
    def __init__(
        self,
        aliyun_uids: List[str] = None,
        batch_quota_application_id: str = None,
        fail_results: List[main_models.CreateQuotaApplicationsForTemplateResponseBodyFailResults] = None,
        request_id: str = None,
    ):
        # The list of Alibaba Cloud accounts that belong to the resource directory members for which quotas are applied.
        self.aliyun_uids = aliyun_uids
        # The batch ID of the quota application.
        self.batch_quota_application_id = batch_quota_application_id
        # The list of Alibaba Cloud accounts that belong to the resource directory members for which quota applications failed and the reasons for the failures.
        self.fail_results = fail_results
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.fail_results:
            for v1 in self.fail_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_uids is not None:
            result['AliyunUids'] = self.aliyun_uids

        if self.batch_quota_application_id is not None:
            result['BatchQuotaApplicationId'] = self.batch_quota_application_id

        result['FailResults'] = []
        if self.fail_results is not None:
            for k1 in self.fail_results:
                result['FailResults'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUids') is not None:
            self.aliyun_uids = m.get('AliyunUids')

        if m.get('BatchQuotaApplicationId') is not None:
            self.batch_quota_application_id = m.get('BatchQuotaApplicationId')

        self.fail_results = []
        if m.get('FailResults') is not None:
            for k1 in m.get('FailResults'):
                temp_model = main_models.CreateQuotaApplicationsForTemplateResponseBodyFailResults()
                self.fail_results.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateQuotaApplicationsForTemplateResponseBodyFailResults(DaraModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        reason: str = None,
    ):
        # The Alibaba Cloud account that belongs to the resource directory member for which the quota application failed.
        self.aliyun_uid = aliyun_uid
        # The reason for the failure.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

