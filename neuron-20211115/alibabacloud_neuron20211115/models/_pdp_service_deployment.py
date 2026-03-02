# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PdpServiceDeployment(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        application_type: str = None,
        change_order_id: str = None,
        context: str = None,
        cpu: int = None,
        deployment_type: str = None,
        description: str = None,
        edas_id: str = None,
        enterprise_id: int = None,
        env: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        image_id: str = None,
        image_tag: str = None,
        instance_count: int = None,
        is_service_group_enable: int = None,
        memory: int = None,
        message: str = None,
        org_type: str = None,
        pbc_id: int = None,
        pbc_name: str = None,
        pipeline_times: int = None,
        repository_id: str = None,
        request_id: str = None,
        rollback_status: str = None,
        service_group_id: int = None,
        service_id: int = None,
        service_name: str = None,
        status: str = None,
        timeout: int = None,
        times: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        self.application_type = application_type
        self.change_order_id = change_order_id
        self.context = context
        # This parameter is required.
        self.cpu = cpu
        self.deployment_type = deployment_type
        self.description = description
        # This parameter is required.
        self.edas_id = edas_id
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # This parameter is required.
        self.env = env
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.image_id = image_id
        # This parameter is required.
        self.image_tag = image_tag
        # This parameter is required.
        self.instance_count = instance_count
        self.is_service_group_enable = is_service_group_enable
        # This parameter is required.
        self.memory = memory
        self.message = message
        self.org_type = org_type
        # This parameter is required.
        self.pbc_id = pbc_id
        # This parameter is required.
        self.pbc_name = pbc_name
        self.pipeline_times = pipeline_times
        self.repository_id = repository_id
        self.request_id = request_id
        self.rollback_status = rollback_status
        self.service_group_id = service_group_id
        # This parameter is required.
        self.service_id = service_id
        # This parameter is required.
        self.service_name = service_name
        # This parameter is required.
        self.status = status
        self.timeout = timeout
        self.times = times
        # This parameter is required.
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

        if self.application_type is not None:
            result['applicationType'] = self.application_type

        if self.change_order_id is not None:
            result['changeOrderId'] = self.change_order_id

        if self.context is not None:
            result['context'] = self.context

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.deployment_type is not None:
            result['deploymentType'] = self.deployment_type

        if self.description is not None:
            result['description'] = self.description

        if self.edas_id is not None:
            result['edasId'] = self.edas_id

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.env is not None:
            result['env'] = self.env

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.image_id is not None:
            result['imageId'] = self.image_id

        if self.image_tag is not None:
            result['imageTag'] = self.image_tag

        if self.instance_count is not None:
            result['instanceCount'] = self.instance_count

        if self.is_service_group_enable is not None:
            result['isServiceGroupEnable'] = self.is_service_group_enable

        if self.memory is not None:
            result['memory'] = self.memory

        if self.message is not None:
            result['message'] = self.message

        if self.org_type is not None:
            result['orgType'] = self.org_type

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        if self.pbc_name is not None:
            result['pbcName'] = self.pbc_name

        if self.pipeline_times is not None:
            result['pipelineTimes'] = self.pipeline_times

        if self.repository_id is not None:
            result['repositoryId'] = self.repository_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.rollback_status is not None:
            result['rollbackStatus'] = self.rollback_status

        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.status is not None:
            result['status'] = self.status

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.times is not None:
            result['times'] = self.times

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('applicationType') is not None:
            self.application_type = m.get('applicationType')

        if m.get('changeOrderId') is not None:
            self.change_order_id = m.get('changeOrderId')

        if m.get('context') is not None:
            self.context = m.get('context')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('deploymentType') is not None:
            self.deployment_type = m.get('deploymentType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('edasId') is not None:
            self.edas_id = m.get('edasId')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')

        if m.get('imageTag') is not None:
            self.image_tag = m.get('imageTag')

        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')

        if m.get('isServiceGroupEnable') is not None:
            self.is_service_group_enable = m.get('isServiceGroupEnable')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('orgType') is not None:
            self.org_type = m.get('orgType')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('pbcName') is not None:
            self.pbc_name = m.get('pbcName')

        if m.get('pipelineTimes') is not None:
            self.pipeline_times = m.get('pipelineTimes')

        if m.get('repositoryId') is not None:
            self.repository_id = m.get('repositoryId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('rollbackStatus') is not None:
            self.rollback_status = m.get('rollbackStatus')

        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('times') is not None:
            self.times = m.get('times')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

