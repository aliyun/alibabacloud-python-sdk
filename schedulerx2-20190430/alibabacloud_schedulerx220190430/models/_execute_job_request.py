# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteJobRequest(DaraModel):
    def __init__(
        self,
        check_job_status: bool = None,
        designate_type: int = None,
        group_id: str = None,
        instance_parameters: str = None,
        job_id: int = None,
        label: str = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
        worker: str = None,
    ):
        # Specifies whether to check the job status. Valid values: -**true**: The job can be run only if the job is enabled. -**false**: The job can be run even if the job is disabled.
        self.check_job_status = check_job_status
        # The type of the designated machine. Valid values: -**1**: worker. -**2**: label.
        self.designate_type = designate_type
        # The application ID. You can obtain the application ID on the Application Management page in the SchedulerX console.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The parameters that are passed to trigger the job to run. The input value can be a random string. The parameters that are passed are obtained by calling the `context.getInstanceParameters()` class in the `processor` code. The parameters are different from custom parameters for creating jobs.
        self.instance_parameters = instance_parameters
        # The job ID. You can obtain the job ID on the Task Management page in the SchedulerX console.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The label of the worker.
        self.label = label
        # The namespace ID. You can obtain the namespace ID on the Namespace page in the SchedulerX console.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The source of the namespace. This parameter is required only for a special third party.
        self.namespace_source = namespace_source
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The worker address of the application. To query the worker address, call the GetWokerList operation.
        self.worker = worker

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_job_status is not None:
            result['CheckJobStatus'] = self.check_job_status

        if self.designate_type is not None:
            result['DesignateType'] = self.designate_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_parameters is not None:
            result['InstanceParameters'] = self.instance_parameters

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.label is not None:
            result['Label'] = self.label

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.worker is not None:
            result['Worker'] = self.worker

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckJobStatus') is not None:
            self.check_job_status = m.get('CheckJobStatus')

        if m.get('DesignateType') is not None:
            self.designate_type = m.get('DesignateType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceParameters') is not None:
            self.instance_parameters = m.get('InstanceParameters')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Worker') is not None:
            self.worker = m.get('Worker')

        return self

