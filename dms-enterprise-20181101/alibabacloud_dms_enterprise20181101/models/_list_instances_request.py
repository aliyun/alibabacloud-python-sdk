# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstancesRequest(DaraModel):
    def __init__(
        self,
        db_type: str = None,
        env_type: str = None,
        instance_source: str = None,
        instance_state: str = None,
        net_type: str = None,
        page_number: int = None,
        page_size: int = None,
        real_login_user_uid: str = None,
        region: str = None,
        search_key: str = None,
        tid: int = None,
    ):
        # The type of the database. For more information about the valid values of this parameter, see [DbType parameter](https://help.aliyun.com/document_detail/198106.html).
        self.db_type = db_type
        # The type of the environment to which the database instance belongs. Valid values:
        # 
        # *   **product:** production environment
        # *   **dev**: development environment
        # *   **pre**: pre-release environment
        # *   **test**: test environment
        # *   **sit**: system integration testing (SIT) environment
        # *   **uat**: user acceptance testing (UAT) environment
        # *   **pet**: stress testing environment
        # *   **stag:** staging environment
        self.env_type = env_type
        # The source of the database instance. Valid values:
        # 
        # *   **PUBLIC_OWN**: a self-managed database instance that is deployed on the Internet
        # *   **RDS**: an ApsaraDB RDS instance
        # *   **ECS_OWN**: a self-managed database that is deployed on an Elastic Compute Service (ECS) instance
        # *   **VPC_IDC**: a self-managed database instance that is deployed in a data center connected over a virtual private cloud (VPC)
        self.instance_source = instance_source
        # The status of the database instance. Valid values:
        # 
        # *   **NORMAL**
        # *   **DISABLE**
        self.instance_state = instance_state
        # The network type of the database instance. Valid values:
        # 
        # *   **CLASSIC:** classic network
        # *   **VPC:** VPC
        self.net_type = net_type
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page. The number cannot exceed 100.
        self.page_size = page_size
        self.real_login_user_uid = real_login_user_uid
        self.region = region
        # The keyword that is used to search for database instances.
        self.search_key = search_key
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to obtain the tenant ID.
        self.tid = tid

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

        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source

        if self.instance_state is not None:
            result['InstanceState'] = self.instance_state

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.real_login_user_uid is not None:
            result['RealLoginUserUid'] = self.real_login_user_uid

        if self.region is not None:
            result['Region'] = self.region

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')

        if m.get('InstanceState') is not None:
            self.instance_state = m.get('InstanceState')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RealLoginUserUid') is not None:
            self.real_login_user_uid = m.get('RealLoginUserUid')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

