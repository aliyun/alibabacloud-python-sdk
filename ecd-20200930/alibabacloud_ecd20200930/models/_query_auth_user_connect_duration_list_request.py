# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAuthUserConnectDurationListRequest(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        data_date: str = None,
        is_ad_user: bool = None,
        next_token: str = None,
        page_num: int = None,
        page_size: int = None,
        statistic_type: str = None,
        threshold: int = None,
        user_name: str = None,
        with_detail: bool = None,
    ):
        # The comparison operator for connection duration. This parameter is used together with Threshold to filter users by a threshold. Valid values:
        # 
        # - GreaterThanThreshold: greater than the threshold.
        # - LessThanThreshold: less than the threshold.
        self.comparison_operator = comparison_operator
        # The date for the statistics, in the yyyy-MM-dd format. If this parameter is left empty, statistics from the previous day are returned by default.
        self.data_date = data_date
        # Specifies whether to query only Active Directory (AD) users. This parameter is required when UserName or WithDetail is specified.
        self.is_ad_user = is_ad_user
        # The paging token. This parameter is used only when statistics are collected by individual session details (StatisticType=SingleSession). You do not need to specify this parameter for the first request. For subsequent requests, set this parameter to the NextToken value returned in the previous response to retrieve the next page.
        self.next_token = next_token
        # The page number, starting from 1. Default value: 1. This parameter takes effect only when statistics are collected by daily cumulative duration (StatisticType=Daily).
        self.page_num = page_num
        # The number of entries per page. Default value: 100. Maximum value: 100.
        self.page_size = page_size
        # The statistics type. Valid values:
        # 
        # - Daily: collects statistics by daily cumulative connection duration. This is the default value.
        # - SingleSession: collects statistics by individual session details.
        self.statistic_type = statistic_type
        # The connection duration threshold, in seconds. This parameter must be used together with ComparisonOperator.
        self.threshold = threshold
        # The name of the end user. Fuzzy match is supported. When you use this parameter, you must also specify IsAdUser.
        self.user_name = user_name
        # Specifies whether to backfill user details such as display name and nickname. This parameter supports both AD users and convenience users. When you use this parameter, you must also specify IsAdUser.
        self.with_detail = with_detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        if self.data_date is not None:
            result['DataDate'] = self.data_date

        if self.is_ad_user is not None:
            result['IsAdUser'] = self.is_ad_user

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.statistic_type is not None:
            result['StatisticType'] = self.statistic_type

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.with_detail is not None:
            result['WithDetail'] = self.with_detail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('DataDate') is not None:
            self.data_date = m.get('DataDate')

        if m.get('IsAdUser') is not None:
            self.is_ad_user = m.get('IsAdUser')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StatisticType') is not None:
            self.statistic_type = m.get('StatisticType')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('WithDetail') is not None:
            self.with_detail = m.get('WithDetail')

        return self

