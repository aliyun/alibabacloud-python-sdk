# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PdpServiceGroupDetail(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        alias: str = None,
        description: str = None,
        edas_id: str = None,
        enterprise_id: int = None,
        env: str = None,
        env_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        group_type: str = None,
        id: int = None,
        log_project: str = None,
        log_store: str = None,
        name: str = None,
        org_type: str = None,
        pbc_id: int = None,
        pipeline_id: str = None,
        product_id: int = None,
        product_name: str = None,
        region: str = None,
        request_id: str = None,
        service_id: int = None,
        type: str = None,
    ):
        self.account_id = account_id
        self.alias = alias
        self.description = description
        self.edas_id = edas_id
        self.enterprise_id = enterprise_id
        self.env = env
        self.env_type = env_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.group_type = group_type
        # This parameter is required.
        self.id = id
        self.log_project = log_project
        self.log_store = log_store
        self.name = name
        self.org_type = org_type
        self.pbc_id = pbc_id
        self.pipeline_id = pipeline_id
        self.product_id = product_id
        self.product_name = product_name
        self.region = region
        self.request_id = request_id
        self.service_id = service_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.alias is not None:
            result['alias'] = self.alias

        if self.description is not None:
            result['description'] = self.description

        if self.edas_id is not None:
            result['edasId'] = self.edas_id

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.env is not None:
            result['env'] = self.env

        if self.env_type is not None:
            result['envType'] = self.env_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.group_type is not None:
            result['groupType'] = self.group_type

        if self.id is not None:
            result['id'] = self.id

        if self.log_project is not None:
            result['logProject'] = self.log_project

        if self.log_store is not None:
            result['logStore'] = self.log_store

        if self.name is not None:
            result['name'] = self.name

        if self.org_type is not None:
            result['orgType'] = self.org_type

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.product_name is not None:
            result['productName'] = self.product_name

        if self.region is not None:
            result['region'] = self.region

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('edasId') is not None:
            self.edas_id = m.get('edasId')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('envType') is not None:
            self.env_type = m.get('envType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('logProject') is not None:
            self.log_project = m.get('logProject')

        if m.get('logStore') is not None:
            self.log_store = m.get('logStore')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('orgType') is not None:
            self.org_type = m.get('orgType')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

