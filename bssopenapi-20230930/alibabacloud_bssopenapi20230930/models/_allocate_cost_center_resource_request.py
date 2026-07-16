# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class AllocateCostCenterResourceRequest(DaraModel):
    def __init__(
        self,
        from_cost_center_id: int = None,
        from_owner_account_id: int = None,
        nbid: str = None,
        resource_instance_list: List[main_models.AllocateCostCenterResourceRequestResourceInstanceList] = None,
        to_cost_center_id: int = None,
    ):
        # The ID of the source cost center. This parameter is required.
        # 
        # - 0 indicates that the cost center is unallocated.
        # - A value greater than 0 indicates an allocated cost center ID.
        self.from_cost_center_id = from_cost_center_id
        # The ID of the owner of the source cost center.
        self.from_owner_account_id = from_owner_account_id
        # The primary sales channel ID. If this parameter is left empty, the sales channel ID of the current user is used by default.
        self.nbid = nbid
        # The list of resource instances.
        # 
        # This parameter is required.
        self.resource_instance_list = resource_instance_list
        # The ID of the destination cost center. Valid values:
        # 
        # - -1: moves the allocated resource to the unallocated state.
        # - A value greater than 0: allocates the resource to the specified cost center.
        self.to_cost_center_id = to_cost_center_id

    def validate(self):
        if self.resource_instance_list:
            for v1 in self.resource_instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_cost_center_id is not None:
            result['FromCostCenterId'] = self.from_cost_center_id

        if self.from_owner_account_id is not None:
            result['FromOwnerAccountId'] = self.from_owner_account_id

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        result['ResourceInstanceList'] = []
        if self.resource_instance_list is not None:
            for k1 in self.resource_instance_list:
                result['ResourceInstanceList'].append(k1.to_map() if k1 else None)

        if self.to_cost_center_id is not None:
            result['ToCostCenterId'] = self.to_cost_center_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromCostCenterId') is not None:
            self.from_cost_center_id = m.get('FromCostCenterId')

        if m.get('FromOwnerAccountId') is not None:
            self.from_owner_account_id = m.get('FromOwnerAccountId')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        self.resource_instance_list = []
        if m.get('ResourceInstanceList') is not None:
            for k1 in m.get('ResourceInstanceList'):
                temp_model = main_models.AllocateCostCenterResourceRequestResourceInstanceList()
                self.resource_instance_list.append(temp_model.from_map(k1))

        if m.get('ToCostCenterId') is not None:
            self.to_cost_center_id = m.get('ToCostCenterId')

        return self

class AllocateCostCenterResourceRequestResourceInstanceList(DaraModel):
    def __init__(
        self,
        apportion_code: str = None,
        apportion_name: str = None,
        commodity_code: str = None,
        commodity_name: str = None,
        instance_id: str = None,
        pip_code: str = None,
        related_resources: str = None,
        resource_group: str = None,
        resource_id: str = None,
        resource_nick: str = None,
        resource_source: str = None,
        resource_status: str = None,
        resource_tag: str = None,
        resource_type: str = None,
        resource_user_id: int = None,
        resource_user_name: str = None,
    ):
        # The attached resource type of the attached-resource instance. This parameter is required only for attached-resource product instances.
        # - Currently, eight commodities support attached resources. The commodity codes are oss, dcdn, snapshot, vod, cdn, live, and cbwp.
        # - You can call the QueryCostUnitResource operation to obtain all billing instances (including attached-resource instances with their attached resources) under a specific cost center (including the unallocated cost center) of a user.
        self.apportion_code = apportion_code
        # The attached resource name.
        self.apportion_name = apportion_name
        # The commodity code of the billing instance. This parameter is required.
        self.commodity_code = commodity_code
        # The commodity name of the resource.
        self.commodity_name = commodity_name
        # The billing granularity ID. This parameter is required.
        self.instance_id = instance_id
        # The product code, which is the same as the product code in User Center bills.
        self.pip_code = pip_code
        # The resources related to the resource instance.
        self.related_resources = related_resources
        # The resource group.
        self.resource_group = resource_group
        # The resource ID.
        self.resource_id = resource_id
        # The custom nickname of the resource.
        self.resource_nick = resource_nick
        # The resource source. Valid values:
        # - AUTO_ALLOCATE: automatic allocation.
        # - MANUAL_ALLOCATE: manual allocation.
        self.resource_source = resource_source
        # The resource status.
        self.resource_status = resource_status
        # The tag of the resource.
        self.resource_tag = resource_tag
        # The resource type.
        self.resource_type = resource_type
        # The ID of the owner of the billing instance. This parameter is required.
        self.resource_user_id = resource_user_id
        # The resource ownership username.
        self.resource_user_name = resource_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apportion_code is not None:
            result['ApportionCode'] = self.apportion_code

        if self.apportion_name is not None:
            result['ApportionName'] = self.apportion_name

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.pip_code is not None:
            result['PipCode'] = self.pip_code

        if self.related_resources is not None:
            result['RelatedResources'] = self.related_resources

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_nick is not None:
            result['ResourceNick'] = self.resource_nick

        if self.resource_source is not None:
            result['ResourceSource'] = self.resource_source

        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status

        if self.resource_tag is not None:
            result['ResourceTag'] = self.resource_tag

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resource_user_id is not None:
            result['ResourceUserId'] = self.resource_user_id

        if self.resource_user_name is not None:
            result['ResourceUserName'] = self.resource_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApportionCode') is not None:
            self.apportion_code = m.get('ApportionCode')

        if m.get('ApportionName') is not None:
            self.apportion_name = m.get('ApportionName')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')

        if m.get('RelatedResources') is not None:
            self.related_resources = m.get('RelatedResources')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceNick') is not None:
            self.resource_nick = m.get('ResourceNick')

        if m.get('ResourceSource') is not None:
            self.resource_source = m.get('ResourceSource')

        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')

        if m.get('ResourceTag') is not None:
            self.resource_tag = m.get('ResourceTag')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ResourceUserId') is not None:
            self.resource_user_id = m.get('ResourceUserId')

        if m.get('ResourceUserName') is not None:
            self.resource_user_name = m.get('ResourceUserName')

        return self

