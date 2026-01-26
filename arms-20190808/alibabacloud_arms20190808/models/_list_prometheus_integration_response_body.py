# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListPrometheusIntegrationResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListPrometheusIntegrationResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The queried exporters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListPrometheusIntegrationResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPrometheusIntegrationResponseBodyData(DaraModel):
    def __init__(
        self,
        can_delete: bool = None,
        can_editor: bool = None,
        cluster_id: str = None,
        container_name: str = None,
        describe: str = None,
        exporter_type: str = None,
        instance_id: int = None,
        instance_name: str = None,
        integration_type: str = None,
        namespace: str = None,
        need_upgrade: bool = None,
        param: str = None,
        pod_name: str = None,
        show_describe: bool = None,
        show_log: bool = None,
        status: str = None,
        target: str = None,
        version: str = None,
    ):
        # Indicates whether the exporter can be deleted.
        self.can_delete = can_delete
        # Indicates whether the exporter can be edited.
        self.can_editor = can_editor
        # The ID of the Prometheus instance.
        self.cluster_id = cluster_id
        # The name of the container.
        self.container_name = container_name
        # The description of the exporter.
        self.describe = describe
        # The type of the exporter.
        self.exporter_type = exporter_type
        # The ID of the exporter.
        self.instance_id = instance_id
        # The name of the exporter.
        self.instance_name = instance_name
        # The integration type. Valid values: kafka, mysql, redis, snmp, emr, nubela, and tidb.
        self.integration_type = integration_type
        # The namespace.
        self.namespace = namespace
        # Indicates whether an upgrade is required.
        self.need_upgrade = need_upgrade
        # The configurations of the exporter. The value is a JSON string.
        self.param = param
        # The pod name of the exporter.
        self.pod_name = pod_name
        # Indicates whether the description is displayed.
        self.show_describe = show_describe
        # Indicates whether the exporter logs are displayed.
        self.show_log = show_log
        # The status of the exporter.
        self.status = status
        # The monitored IP address.
        self.target = target
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_delete is not None:
            result['CanDelete'] = self.can_delete

        if self.can_editor is not None:
            result['CanEditor'] = self.can_editor

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.describe is not None:
            result['Describe'] = self.describe

        if self.exporter_type is not None:
            result['ExporterType'] = self.exporter_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.need_upgrade is not None:
            result['NeedUpgrade'] = self.need_upgrade

        if self.param is not None:
            result['Param'] = self.param

        if self.pod_name is not None:
            result['PodName'] = self.pod_name

        if self.show_describe is not None:
            result['ShowDescribe'] = self.show_describe

        if self.show_log is not None:
            result['ShowLog'] = self.show_log

        if self.status is not None:
            result['Status'] = self.status

        if self.target is not None:
            result['Target'] = self.target

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanDelete') is not None:
            self.can_delete = m.get('CanDelete')

        if m.get('CanEditor') is not None:
            self.can_editor = m.get('CanEditor')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('Describe') is not None:
            self.describe = m.get('Describe')

        if m.get('ExporterType') is not None:
            self.exporter_type = m.get('ExporterType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NeedUpgrade') is not None:
            self.need_upgrade = m.get('NeedUpgrade')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')

        if m.get('ShowDescribe') is not None:
            self.show_describe = m.get('ShowDescribe')

        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

