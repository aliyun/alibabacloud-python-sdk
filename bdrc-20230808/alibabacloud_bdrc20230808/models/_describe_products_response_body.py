# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class DescribeProductsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeProductsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeProductsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeProductsResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.DescribeProductsResponseBodyDataContent] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # A list of cloud products and their data protection status.
        self.content = content
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The token for the next page of results. If this parameter is absent from the response, all results have been retrieved.
        self.next_token = next_token
        # The total number of entries that match the query. This parameter is not returned by default.
        self.total_count = total_count

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.DescribeProductsResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeProductsResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        check_failed_count: int = None,
        check_failed_resource_count: int = None,
        disable_check_resource_count: int = None,
        enable_check: bool = None,
        product_type: str = None,
        protection_score: int = None,
        protection_score_distribution: List[main_models.DescribeProductsResponseBodyDataContentProtectionScoreDistribution] = None,
        protection_score_updated_time: int = None,
        risk_count: int = None,
        risky_resource_count: int = None,
        total_resource_count: int = None,
        wait_for_check_resource_count: int = None,
    ):
        # The count of failed check items.
        self.check_failed_count = check_failed_count
        # The count of resources that failed the check.
        self.check_failed_resource_count = check_failed_resource_count
        # The count of resources for which the check is disabled.
        self.disable_check_resource_count = disable_check_resource_count
        # Indicates whether the data protection score is enabled for the cloud product.
        self.enable_check = enable_check
        # The cloud product type, such as `ECS` and `OSS`.
        self.product_type = product_type
        # The data protection score, ranging from 0 to 100.
        self.protection_score = protection_score
        # The distribution of resources across different score ranges.
        self.protection_score_distribution = protection_score_distribution
        # The UNIX timestamp of the last data protection score update.
        self.protection_score_updated_time = protection_score_updated_time
        # The count of risky check items.
        self.risk_count = risk_count
        # The count of risky resources.
        self.risky_resource_count = risky_resource_count
        # The total count of resources for the cloud product.
        self.total_resource_count = total_resource_count
        # The count of resources pending a check.
        self.wait_for_check_resource_count = wait_for_check_resource_count

    def validate(self):
        if self.protection_score_distribution:
            for v1 in self.protection_score_distribution:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_failed_count is not None:
            result['CheckFailedCount'] = self.check_failed_count

        if self.check_failed_resource_count is not None:
            result['CheckFailedResourceCount'] = self.check_failed_resource_count

        if self.disable_check_resource_count is not None:
            result['DisableCheckResourceCount'] = self.disable_check_resource_count

        if self.enable_check is not None:
            result['EnableCheck'] = self.enable_check

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.protection_score is not None:
            result['ProtectionScore'] = self.protection_score

        result['ProtectionScoreDistribution'] = []
        if self.protection_score_distribution is not None:
            for k1 in self.protection_score_distribution:
                result['ProtectionScoreDistribution'].append(k1.to_map() if k1 else None)

        if self.protection_score_updated_time is not None:
            result['ProtectionScoreUpdatedTime'] = self.protection_score_updated_time

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.risky_resource_count is not None:
            result['RiskyResourceCount'] = self.risky_resource_count

        if self.total_resource_count is not None:
            result['TotalResourceCount'] = self.total_resource_count

        if self.wait_for_check_resource_count is not None:
            result['WaitForCheckResourceCount'] = self.wait_for_check_resource_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckFailedCount') is not None:
            self.check_failed_count = m.get('CheckFailedCount')

        if m.get('CheckFailedResourceCount') is not None:
            self.check_failed_resource_count = m.get('CheckFailedResourceCount')

        if m.get('DisableCheckResourceCount') is not None:
            self.disable_check_resource_count = m.get('DisableCheckResourceCount')

        if m.get('EnableCheck') is not None:
            self.enable_check = m.get('EnableCheck')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ProtectionScore') is not None:
            self.protection_score = m.get('ProtectionScore')

        self.protection_score_distribution = []
        if m.get('ProtectionScoreDistribution') is not None:
            for k1 in m.get('ProtectionScoreDistribution'):
                temp_model = main_models.DescribeProductsResponseBodyDataContentProtectionScoreDistribution()
                self.protection_score_distribution.append(temp_model.from_map(k1))

        if m.get('ProtectionScoreUpdatedTime') is not None:
            self.protection_score_updated_time = m.get('ProtectionScoreUpdatedTime')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('RiskyResourceCount') is not None:
            self.risky_resource_count = m.get('RiskyResourceCount')

        if m.get('TotalResourceCount') is not None:
            self.total_resource_count = m.get('TotalResourceCount')

        if m.get('WaitForCheckResourceCount') is not None:
            self.wait_for_check_resource_count = m.get('WaitForCheckResourceCount')

        return self

class DescribeProductsResponseBodyDataContentProtectionScoreDistribution(DaraModel):
    def __init__(
        self,
        count: int = None,
        range: main_models.DescribeProductsResponseBodyDataContentProtectionScoreDistributionRange = None,
    ):
        # The count of resources within this score range.
        self.count = count
        # The score range.
        self.range = range

    def validate(self):
        if self.range:
            self.range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.range is not None:
            result['Range'] = self.range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Range') is not None:
            temp_model = main_models.DescribeProductsResponseBodyDataContentProtectionScoreDistributionRange()
            self.range = temp_model.from_map(m.get('Range'))

        return self

class DescribeProductsResponseBodyDataContentProtectionScoreDistributionRange(DaraModel):
    def __init__(
        self,
        from_: int = None,
        to: int = None,
    ):
        # The lower bound of the score range, inclusive.
        self.from_ = from_
        # The upper bound of the score range, inclusive.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

