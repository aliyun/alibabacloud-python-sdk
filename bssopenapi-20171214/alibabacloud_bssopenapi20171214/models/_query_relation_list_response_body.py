# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryRelationListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryRelationListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryRelationListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryRelationListResponseBodyData(DaraModel):
    def __init__(
        self,
        financial_relation_info_list: List[main_models.QueryRelationListResponseBodyDataFinancialRelationInfoList] = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The relationships.
        self.financial_relation_info_list = financial_relation_info_list
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.financial_relation_info_list:
            for v1 in self.financial_relation_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FinancialRelationInfoList'] = []
        if self.financial_relation_info_list is not None:
            for k1 in self.financial_relation_info_list:
                result['FinancialRelationInfoList'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.financial_relation_info_list = []
        if m.get('FinancialRelationInfoList') is not None:
            for k1 in m.get('FinancialRelationInfoList'):
                temp_model = main_models.QueryRelationListResponseBodyDataFinancialRelationInfoList()
                self.financial_relation_info_list.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryRelationListResponseBodyDataFinancialRelationInfoList(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        account_name: str = None,
        account_nick_name: str = None,
        account_type: str = None,
        end_time: str = None,
        relation_id: int = None,
        relation_type: str = None,
        setup_time: str = None,
        start_time: str = None,
        state: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The name of the account.
        self.account_name = account_name
        # The display name of the account.
        self.account_nick_name = account_nick_name
        # The type of the account. Valid values: MASTER and MEMBER.
        self.account_type = account_type
        # The time when the relationship became invalid. If no value is returned, the relationship is still valid.
        self.end_time = end_time
        # The ID of the relationship.
        self.relation_id = relation_id
        # The type of the relationship. Valid values: FinancialManagement and FinancialTrusteeship.
        self.relation_type = relation_type
        # The time when the relationship was established. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC. Example: 2016-05-23T12:00:00Z.
        self.setup_time = setup_time
        # The time when the relationship became valid. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC. Example: 2016-05-23T12:00:00Z.
        self.start_time = start_time
        # The state of the relationship. One of the enumeration members of the RelationshipStatusEnum data type is returned.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_nick_name is not None:
            result['AccountNickName'] = self.account_nick_name

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.relation_id is not None:
            result['RelationId'] = self.relation_id

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.setup_time is not None:
            result['SetupTime'] = self.setup_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountNickName') is not None:
            self.account_nick_name = m.get('AccountNickName')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('SetupTime') is not None:
            self.setup_time = m.get('SetupTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

