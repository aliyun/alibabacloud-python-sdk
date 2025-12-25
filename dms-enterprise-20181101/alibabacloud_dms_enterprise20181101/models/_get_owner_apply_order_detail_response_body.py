# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetOwnerApplyOrderDetailResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        owner_apply_order_detail: main_models.GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetail = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The details of the ticket.
        self.owner_apply_order_detail = owner_apply_order_detail
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.owner_apply_order_detail:
            self.owner_apply_order_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.owner_apply_order_detail is not None:
            result['OwnerApplyOrderDetail'] = self.owner_apply_order_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('OwnerApplyOrderDetail') is not None:
            temp_model = main_models.GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetail()
            self.owner_apply_order_detail = temp_model.from_map(m.get('OwnerApplyOrderDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetail(DaraModel):
    def __init__(
        self,
        apply_type: str = None,
        resources: List[main_models.GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResources] = None,
    ):
        # The type of the submitted ticket. Valid values:
        # 
        # *   **INSTANCE**: the ticket that applies for the permissions to be an instance owner
        # *   **DB**: the ticket that applies for the permissions to be a database owner
        # *   **TABLE**: the ticket that applies for the permissions to be a table owner
        self.apply_type = apply_type
        # The details of the requested resource.
        self.resources = resources

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResources()
                self.resources.append(temp_model.from_map(k1))

        return self

class GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResources(DaraModel):
    def __init__(
        self,
        logic: bool = None,
        resource_detail: main_models.GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResourcesResourceDetail = None,
        target_id: str = None,
    ):
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true**: The instance is a logical database.
        # *   **false**: The instance is not a logical database.
        self.logic = logic
        # The details of the resource.
        self.resource_detail = resource_detail
        # The ID of the resource.
        self.target_id = target_id

    def validate(self):
        if self.resource_detail:
            self.resource_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logic is not None:
            result['Logic'] = self.logic

        if self.resource_detail is not None:
            result['ResourceDetail'] = self.resource_detail.to_map()

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('ResourceDetail') is not None:
            temp_model = main_models.GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResourcesResourceDetail()
            self.resource_detail = temp_model.from_map(m.get('ResourceDetail'))

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        return self

class GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResourcesResourceDetail(DaraModel):
    def __init__(
        self,
        db_type: str = None,
        env_type: str = None,
        owner_ids: List[int] = None,
        owner_nick_names: List[str] = None,
        search_name: str = None,
        table_name: str = None,
    ):
        # The type of the database engine.
        self.db_type = db_type
        # The type of the environment to which the instance belongs. For more information, see [Change the environment type of an instance](https://help.aliyun.com/document_detail/163309.html).
        self.env_type = env_type
        # The IDs of the original owners.
        self.owner_ids = owner_ids
        # The nicknames of the owners.
        self.owner_nick_names = owner_nick_names
        # The search name of the resource.
        self.search_name = search_name
        # The name of the table.
        # 
        # > : This parameter is returned when you submit a Database-OWNER ticket.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids

        if self.owner_nick_names is not None:
            result['OwnerNickNames'] = self.owner_nick_names

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')

        if m.get('OwnerNickNames') is not None:
            self.owner_nick_names = m.get('OwnerNickNames')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

