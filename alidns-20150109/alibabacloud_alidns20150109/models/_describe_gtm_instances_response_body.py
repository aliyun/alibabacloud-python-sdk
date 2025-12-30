# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeGtmInstancesResponseBody(DaraModel):
    def __init__(
        self,
        gtm_instances: main_models.DescribeGtmInstancesResponseBodyGtmInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The list of queried instances.
        self.gtm_instances = gtm_instances
        # The returned page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_items = total_items
        # The total number of pages returned.
        self.total_pages = total_pages

    def validate(self):
        if self.gtm_instances:
            self.gtm_instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gtm_instances is not None:
            result['GtmInstances'] = self.gtm_instances.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GtmInstances') is not None:
            temp_model = main_models.DescribeGtmInstancesResponseBodyGtmInstances()
            self.gtm_instances = temp_model.from_map(m.get('GtmInstances'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeGtmInstancesResponseBodyGtmInstances(DaraModel):
    def __init__(
        self,
        gtm_instance: List[main_models.DescribeGtmInstancesResponseBodyGtmInstancesGtmInstance] = None,
    ):
        self.gtm_instance = gtm_instance

    def validate(self):
        if self.gtm_instance:
            for v1 in self.gtm_instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GtmInstance'] = []
        if self.gtm_instance is not None:
            for k1 in self.gtm_instance:
                result['GtmInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gtm_instance = []
        if m.get('GtmInstance') is not None:
            for k1 in m.get('GtmInstance'):
                temp_model = main_models.DescribeGtmInstancesResponseBodyGtmInstancesGtmInstance()
                self.gtm_instance.append(temp_model.from_map(k1))

        return self

class DescribeGtmInstancesResponseBodyGtmInstancesGtmInstance(DaraModel):
    def __init__(
        self,
        access_strategy_num: int = None,
        address_pool_num: int = None,
        alert_group: str = None,
        cname: str = None,
        cname_mode: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        expire_time: str = None,
        expire_timestamp: int = None,
        instance_id: str = None,
        instance_name: str = None,
        lba_strategy: str = None,
        resource_group_id: str = None,
        ttl: int = None,
        user_domain_name: str = None,
        version_code: str = None,
    ):
        # The number of access policies.
        self.access_strategy_num = access_strategy_num
        # The number of address pools.
        self.address_pool_num = address_pool_num
        # The name of the alert group.
        self.alert_group = alert_group
        # The CNAME domain name that is used to access the instance.
        self.cname = cname
        # The CNAME domain name used to access the instance. Valid values:
        # 
        # *   **SYSTEM_ASSIGN**: A CNAME domain name assigned by the system is used.
        # *   **CUSTOM**: A custom CNAME domain name is used.
        self.cname_mode = cname_mode
        # The time when the instance was created.
        self.create_time = create_time
        # The UNIX timestamp that indicates when the instance was created.
        self.create_timestamp = create_timestamp
        # The time when the instance expires.
        self.expire_time = expire_time
        # The UNIX timestamp that indicates when the instance expires.
        self.expire_timestamp = expire_timestamp
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The load balancing policy that is used. Valid values:
        # 
        # *   **ALL_RR**: Load balancing
        # *   **RATIO**: Weighted round-robin
        self.lba_strategy = lba_strategy
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The global time to live (TTL).
        self.ttl = ttl
        # The domain name of the user.
        self.user_domain_name = user_domain_name
        # The version code of the instance.
        self.version_code = version_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_strategy_num is not None:
            result['AccessStrategyNum'] = self.access_strategy_num

        if self.address_pool_num is not None:
            result['AddressPoolNum'] = self.address_pool_num

        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group

        if self.cname is not None:
            result['Cname'] = self.cname

        if self.cname_mode is not None:
            result['CnameMode'] = self.cname_mode

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expire_timestamp is not None:
            result['ExpireTimestamp'] = self.expire_timestamp

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.lba_strategy is not None:
            result['LbaStrategy'] = self.lba_strategy

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.user_domain_name is not None:
            result['UserDomainName'] = self.user_domain_name

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessStrategyNum') is not None:
            self.access_strategy_num = m.get('AccessStrategyNum')

        if m.get('AddressPoolNum') is not None:
            self.address_pool_num = m.get('AddressPoolNum')

        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')

        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('CnameMode') is not None:
            self.cname_mode = m.get('CnameMode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExpireTimestamp') is not None:
            self.expire_timestamp = m.get('ExpireTimestamp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('LbaStrategy') is not None:
            self.lba_strategy = m.get('LbaStrategy')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('UserDomainName') is not None:
            self.user_domain_name = m.get('UserDomainName')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        return self

