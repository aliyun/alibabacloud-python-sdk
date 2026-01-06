# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class DescribeDeploymentJobResponseBody(DaraModel):
    def __init__(
        self,
        cas_contacts: List[main_models.DescribeDeploymentJobResponseBodyCasContacts] = None,
        cert_domain: str = None,
        cert_type: str = None,
        config: str = None,
        del_: int = None,
        end_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: str = None,
        job_type: str = None,
        name: str = None,
        product_name: str = None,
        request_id: str = None,
        rollback: int = None,
        schedule_time: str = None,
        start_time: str = None,
        status: str = None,
        user_id: int = None,
    ):
        # The information about the contact.
        self.cas_contacts = cas_contacts
        # The domain names bound to the certificate of the deployment task.
        self.cert_domain = cert_domain
        # The type of the certificate. Valid values:
        # 
        # *   **upload**: uploaded certificate
        # *   **buy**: purchased certificate
        # *   **free**: free certificate available only on the China site (aliyun.com)
        self.cert_type = cert_type
        # The configurations of the deployment task.
        self.config = config
        # Indicates whether the deployment job was deleted. Valid values:
        # 
        # *   **0**: not deleted
        # *   **1**: deleted
        self.del_ = del_
        # The end time of the deployment job. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The time when the deployment job was created. The value is a UNIX timestamp. Unit: seconds.
        self.gmt_create = gmt_create
        # The time when the deployment job was last modified. The value is a UNIX timestamp. Unit: seconds.
        self.gmt_modified = gmt_modified
        # The ID of the deployment job.
        self.id = id
        # The instance ID of the deployment task.
        self.instance_id = instance_id
        # The type of the deployment job. Valid values:
        # 
        # *   **cloud**: multi-cloud deployment job.
        # *   **trustee**: hosted deployment job available only on the China site (aliyun.com).
        # *   **user**: cloud service deployment job. The cloud server is not included.
        self.job_type = job_type
        # The name of the deployment task.
        self.name = name
        # The cloud services included in the deployment task.
        self.product_name = product_name
        # The request ID.
        self.request_id = request_id
        # Indicates whether the deployment job includes the rollback worker. For example, if a cloud service in a deployment job has been rolled back, **1** is returned. Valid values:
        # 
        # *   **0**: The rollback worker is not included.
        # *   **1**: The rollback worker is included.
        self.rollback = rollback
        # The time when the deployment job was scheduled. The value is a UNIX timestamp. Unit: seconds.
        self.schedule_time = schedule_time
        # The start time of the deployment job. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The status of the deployment job. Valid values:
        # 
        # *   **pending**
        # *   **editing**
        # *   **scheduling**
        # *   **processing**
        # *   **error**
        # *   **success**
        self.status = status
        # The ID of the Alibaba Cloud account in which the deployment job is created.
        self.user_id = user_id

    def validate(self):
        if self.cas_contacts:
            for v1 in self.cas_contacts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CasContacts'] = []
        if self.cas_contacts is not None:
            for k1 in self.cas_contacts:
                result['CasContacts'].append(k1.to_map() if k1 else None)

        if self.cert_domain is not None:
            result['CertDomain'] = self.cert_domain

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.config is not None:
            result['Config'] = self.config

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
        self.cas_contacts = []
        if m.get('CasContacts') is not None:
            for k1 in m.get('CasContacts'):
                temp_model = main_models.DescribeDeploymentJobResponseBodyCasContacts()
                self.cas_contacts.append(temp_model.from_map(k1))

        if m.get('CertDomain') is not None:
            self.cert_domain = m.get('CertDomain')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('Config') is not None:
            self.config = m.get('Config')

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

class DescribeDeploymentJobResponseBodyCasContacts(DaraModel):
    def __init__(
        self,
        email: str = None,
        id: str = None,
        mobile: str = None,
        name: str = None,
    ):
        # The email address of the contact.
        self.email = email
        # The ID of the contact.
        self.id = id
        # The phone number of the contact.
        self.mobile = mobile
        # The name of the contact.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.id is not None:
            result['Id'] = self.id

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

