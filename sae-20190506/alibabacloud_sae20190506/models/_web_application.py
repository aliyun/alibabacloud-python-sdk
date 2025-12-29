# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class WebApplication(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        created_time: str = None,
        description: str = None,
        internet_url: str = None,
        intranet_url: str = None,
        last_modified_time: str = None,
        namespace_id: str = None,
        revision_config: main_models.RevisionConfig = None,
        vpc_id: str = None,
        web_scaling_config: main_models.WebScalingConfig = None,
        web_traffic_config: main_models.WebTrafficConfig = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        # This parameter is required.
        self.application_name = application_name
        self.created_time = created_time
        self.description = description
        self.internet_url = internet_url
        self.intranet_url = intranet_url
        self.last_modified_time = last_modified_time
        self.namespace_id = namespace_id
        self.revision_config = revision_config
        self.vpc_id = vpc_id
        self.web_scaling_config = web_scaling_config
        self.web_traffic_config = web_traffic_config

    def validate(self):
        if self.revision_config:
            self.revision_config.validate()
        if self.web_scaling_config:
            self.web_scaling_config.validate()
        if self.web_traffic_config:
            self.web_traffic_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.internet_url is not None:
            result['InternetURL'] = self.internet_url

        if self.intranet_url is not None:
            result['IntranetURL'] = self.intranet_url

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.revision_config is not None:
            result['RevisionConfig'] = self.revision_config.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.web_scaling_config is not None:
            result['WebScalingConfig'] = self.web_scaling_config.to_map()

        if self.web_traffic_config is not None:
            result['WebTrafficConfig'] = self.web_traffic_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InternetURL') is not None:
            self.internet_url = m.get('InternetURL')

        if m.get('IntranetURL') is not None:
            self.intranet_url = m.get('IntranetURL')

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('RevisionConfig') is not None:
            temp_model = main_models.RevisionConfig()
            self.revision_config = temp_model.from_map(m.get('RevisionConfig'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WebScalingConfig') is not None:
            temp_model = main_models.WebScalingConfig()
            self.web_scaling_config = temp_model.from_map(m.get('WebScalingConfig'))

        if m.get('WebTrafficConfig') is not None:
            temp_model = main_models.WebTrafficConfig()
            self.web_traffic_config = temp_model.from_map(m.get('WebTrafficConfig'))

        return self

