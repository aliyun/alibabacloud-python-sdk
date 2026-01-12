# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class DescribeAppInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeAppInstancesResponseBodyInstances] = None,
        max_results: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the RDS Supabase instances.
        self.instances = instances
        # A reserved parameter. You do not need to specify this parameter.
        self.max_results = max_results
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

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
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeAppInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAppInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        dbinstance_name: str = None,
        instance_class: str = None,
        instance_minor_version: str = None,
        instance_name: str = None,
        public_connection_string: str = None,
        region_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_connection_string: str = None,
    ):
        # The name of the AI application.
        self.app_name = app_name
        # The application type. Only **supabase** is supported. For more information, see [RDS Supabase](https://help.aliyun.com/document_detail/2938735.html).
        self.app_type = app_type
        # The ID of the RDS for PostgreSQL instance with which the RDS Supabase instances are associated.
        self.dbinstance_name = dbinstance_name
        # The instance type.
        self.instance_class = instance_class
        # The minor version number of RDS Supabase instance.
        self.instance_minor_version = instance_minor_version
        # The ID of the RDS Supabase instance.
        self.instance_name = instance_name
        # The public endpoint of the AI application.
        self.public_connection_string = public_connection_string
        # The region ID.
        self.region_id = region_id
        # The instance status. For more information, see [Instance state table](https://help.aliyun.com/document_detail/2623972.html).
        self.status = status
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The internal endpoint of the AI application.
        self.vpc_connection_string = vpc_connection_string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_minor_version is not None:
            result['InstanceMinorVersion'] = self.instance_minor_version

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.public_connection_string is not None:
            result['PublicConnectionString'] = self.public_connection_string

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_connection_string is not None:
            result['VpcConnectionString'] = self.vpc_connection_string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceMinorVersion') is not None:
            self.instance_minor_version = m.get('InstanceMinorVersion')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PublicConnectionString') is not None:
            self.public_connection_string = m.get('PublicConnectionString')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcConnectionString') is not None:
            self.vpc_connection_string = m.get('VpcConnectionString')

        return self

