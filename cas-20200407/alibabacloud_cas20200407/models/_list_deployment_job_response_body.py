# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class ListDeploymentJobResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.ListDeploymentJobResponseBodyData] = None,
        request_id: str = None,
        show_size: int = None,
        total: int = None,
    ):
        # The page number. Default value: 1.
        self.current_page = current_page
        # The data returned for the request.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The number of deployment tasks per page. Default value: **50**.
        self.show_size = show_size
        # The total number of deployment tasks returned.
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDeploymentJobResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListDeploymentJobResponseBodyData(DaraModel):
    def __init__(
        self,
        cert_domain: str = None,
        cert_type: str = None,
        del_: int = None,
        end_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: str = None,
        job_type: str = None,
        name: str = None,
        product_name: str = None,
        rollback: int = None,
        schedule_time: str = None,
        start_time: str = None,
        status: str = None,
        user_id: int = None,
    ):
        # The domain names bound to the certificate of the deployment task.
        self.cert_domain = cert_domain
        # The type of the certificate. Valid values:
        # 
        # *   **upload**: uploaded certificate
        # *   **buy**: purchased certificate
        # *   **free**: free certificate, available only on the China site (aliyun.com)
        self.cert_type = cert_type
        # Indicates whether the deployment task is deleted. Valid values:
        # 
        # *   **0**: not deleted
        # *   **1**: deleted
        self.del_ = del_
        # The end time of the deployment task.
        self.end_time = end_time
        # The time when the deployment task was created.
        self.gmt_create = gmt_create
        # The time when the deployment task was last modified.
        self.gmt_modified = gmt_modified
        # The ID of the deployment task. You can use the ID to query the details and status of the deployment task.
        self.id = id
        # The instance ID of the deployment task.
        self.instance_id = instance_id
        # The type of the deployment task.
        # 
        # *   **cloud**: multi-cloud deployment task.
        # *   **user**: cloud service deployment task. This type of task does not support ECS instances.
        self.job_type = job_type
        # The name of the deployment task.
        self.name = name
        # The cloud service included in the resources of the deployment task.
        self.product_name = product_name
        # Indicates whether the rollback worker is included. For example, if a cloud service involved in a deployment task has been rolled back, **1** is returned. Valid values:
        # 
        # *   **0**: The rollback worker is not included.
        # *   **1**: The rollback worker is included.
        self.rollback = rollback
        # The time when the deployment task was scheduled.
        self.schedule_time = schedule_time
        # The start time of the deployment task.
        self.start_time = start_time
        # The status of the deployment task. Valid values:
        # 
        # *   **pending**
        # *   **editing**
        # *   **scheduling**
        # *   **processing**
        # *   **error**
        # *   **success**
        self.status = status
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_domain is not None:
            result['CertDomain'] = self.cert_domain

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.del_ is not None:
            result['Del'] = self.del_

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.name is not None:
            result['Name'] = self.name

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.rollback is not None:
            result['Rollback'] = self.rollback

        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertDomain') is not None:
            self.cert_domain = m.get('CertDomain')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('Del') is not None:
            self.del_ = m.get('Del')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('Rollback') is not None:
            self.rollback = m.get('Rollback')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

