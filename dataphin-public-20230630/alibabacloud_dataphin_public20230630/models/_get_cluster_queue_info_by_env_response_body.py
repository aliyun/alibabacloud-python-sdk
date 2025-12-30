# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetClusterQueueInfoByEnvResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetClusterQueueInfoByEnvResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetClusterQueueInfoByEnvResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetClusterQueueInfoByEnvResponseBodyData(DaraModel):
    def __init__(
        self,
        annotations: str = None,
        cluster_id: str = None,
        create_at: str = None,
        flink_image_registry: str = None,
        flink_image_repository: str = None,
        flink_image_tag: str = None,
        flink_version: str = None,
        labels: str = None,
        max_vcore: str = None,
        modified_at: str = None,
        namespace: str = None,
        queue_name: str = None,
        resource_version: str = None,
        spec: str = None,
        vvp_cluster_type: str = None,
    ):
        self.annotations = annotations
        self.cluster_id = cluster_id
        self.create_at = create_at
        self.flink_image_registry = flink_image_registry
        self.flink_image_repository = flink_image_repository
        self.flink_image_tag = flink_image_tag
        self.flink_version = flink_version
        self.labels = labels
        self.max_vcore = max_vcore
        self.modified_at = modified_at
        self.namespace = namespace
        self.queue_name = queue_name
        self.resource_version = resource_version
        self.spec = spec
        self.vvp_cluster_type = vvp_cluster_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotations is not None:
            result['Annotations'] = self.annotations

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.create_at is not None:
            result['CreateAt'] = self.create_at

        if self.flink_image_registry is not None:
            result['FlinkImageRegistry'] = self.flink_image_registry

        if self.flink_image_repository is not None:
            result['FlinkImageRepository'] = self.flink_image_repository

        if self.flink_image_tag is not None:
            result['FlinkImageTag'] = self.flink_image_tag

        if self.flink_version is not None:
            result['FlinkVersion'] = self.flink_version

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.max_vcore is not None:
            result['MaxVcore'] = self.max_vcore

        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.resource_version is not None:
            result['ResourceVersion'] = self.resource_version

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.vvp_cluster_type is not None:
            result['VvpClusterType'] = self.vvp_cluster_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CreateAt') is not None:
            self.create_at = m.get('CreateAt')

        if m.get('FlinkImageRegistry') is not None:
            self.flink_image_registry = m.get('FlinkImageRegistry')

        if m.get('FlinkImageRepository') is not None:
            self.flink_image_repository = m.get('FlinkImageRepository')

        if m.get('FlinkImageTag') is not None:
            self.flink_image_tag = m.get('FlinkImageTag')

        if m.get('FlinkVersion') is not None:
            self.flink_version = m.get('FlinkVersion')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('MaxVcore') is not None:
            self.max_vcore = m.get('MaxVcore')

        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('ResourceVersion') is not None:
            self.resource_version = m.get('ResourceVersion')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('VvpClusterType') is not None:
            self.vvp_cluster_type = m.get('VvpClusterType')

        return self

