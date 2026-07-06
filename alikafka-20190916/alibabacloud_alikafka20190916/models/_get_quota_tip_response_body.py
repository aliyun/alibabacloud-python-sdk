# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class GetQuotaTipResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        quota_data: main_models.GetQuotaTipResponseBodyQuotaData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status code. A value of 200 indicates success.
        self.code = code
        # Additional information. In typical scenarios, it provides a brief description of failed calls to help the caller locate the problem
        self.message = message
        # Quota information.
        self.quota_data = quota_data
        # Request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.quota_data:
            self.quota_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.quota_data is not None:
            result['QuotaData'] = self.quota_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('QuotaData') is not None:
            temp_model = main_models.GetQuotaTipResponseBodyQuotaData()
            self.quota_data = temp_model.from_map(m.get('QuotaData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQuotaTipResponseBodyQuotaData(DaraModel):
    def __init__(
        self,
        group_left: int = None,
        group_used: int = None,
        is_partition_buy: int = None,
        partition_left: int = None,
        partition_num_of_buy: int = None,
        partition_quota: int = None,
        partition_used: int = None,
        topic_left: int = None,
        topic_num_of_buy: int = None,
        topic_quota: int = None,
        topic_used: int = None,
    ):
        # Remaining Group quota.
        self.group_left = group_left
        # Used Group quota.
        self.group_used = group_used
        # Partition purchase method distinction, with the following values:
        # 
        # - 0: indicates that the instance uses the topic model for purchase.
        # 
        # - 1: indicates partition model purchase.
        self.is_partition_buy = is_partition_buy
        # Remaining partition quota.
        self.partition_left = partition_left
        # Number of purchased partitions.
        self.partition_num_of_buy = partition_num_of_buy
        # Partition quota.
        self.partition_quota = partition_quota
        # Used partition quota.
        self.partition_used = partition_used
        # Remaining topic quota.
        self.topic_left = topic_left
        # Number of purchased topics.
        self.topic_num_of_buy = topic_num_of_buy
        # Topic quota.
        self.topic_quota = topic_quota
        # Used topic quota.
        self.topic_used = topic_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_left is not None:
            result['GroupLeft'] = self.group_left

        if self.group_used is not None:
            result['GroupUsed'] = self.group_used

        if self.is_partition_buy is not None:
            result['IsPartitionBuy'] = self.is_partition_buy

        if self.partition_left is not None:
            result['PartitionLeft'] = self.partition_left

        if self.partition_num_of_buy is not None:
            result['PartitionNumOfBuy'] = self.partition_num_of_buy

        if self.partition_quota is not None:
            result['PartitionQuota'] = self.partition_quota

        if self.partition_used is not None:
            result['PartitionUsed'] = self.partition_used

        if self.topic_left is not None:
            result['TopicLeft'] = self.topic_left

        if self.topic_num_of_buy is not None:
            result['TopicNumOfBuy'] = self.topic_num_of_buy

        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota

        if self.topic_used is not None:
            result['TopicUsed'] = self.topic_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupLeft') is not None:
            self.group_left = m.get('GroupLeft')

        if m.get('GroupUsed') is not None:
            self.group_used = m.get('GroupUsed')

        if m.get('IsPartitionBuy') is not None:
            self.is_partition_buy = m.get('IsPartitionBuy')

        if m.get('PartitionLeft') is not None:
            self.partition_left = m.get('PartitionLeft')

        if m.get('PartitionNumOfBuy') is not None:
            self.partition_num_of_buy = m.get('PartitionNumOfBuy')

        if m.get('PartitionQuota') is not None:
            self.partition_quota = m.get('PartitionQuota')

        if m.get('PartitionUsed') is not None:
            self.partition_used = m.get('PartitionUsed')

        if m.get('TopicLeft') is not None:
            self.topic_left = m.get('TopicLeft')

        if m.get('TopicNumOfBuy') is not None:
            self.topic_num_of_buy = m.get('TopicNumOfBuy')

        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')

        if m.get('TopicUsed') is not None:
            self.topic_used = m.get('TopicUsed')

        return self

