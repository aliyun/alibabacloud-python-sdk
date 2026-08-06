# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ModelVersion(DaraModel):
    def __init__(
        self,
        approval_status: str = None,
        compression_spec: Dict[str, Any] = None,
        distillation_spec: Dict[str, Any] = None,
        evaluation_spec: Dict[str, Any] = None,
        extra_info: Dict[str, Any] = None,
        format_type: str = None,
        framework_type: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        inference_spec: Dict[str, Any] = None,
        labels: List[main_models.ModelVersionLabels] = None,
        metrics: Dict[str, Any] = None,
        options: str = None,
        owner_id: str = None,
        source_id: str = None,
        source_type: str = None,
        training_spec: Dict[str, Any] = None,
        uri: str = None,
        user_id: str = None,
        version_description: str = None,
        version_name: str = None,
    ):
        # The approval status. Valid values:
        # - Pending: pending.
        # - Approved: approved for going live.
        # - Rejected: not approved for going live.
        self.approval_status = approval_status
        # The compression configuration.
        self.compression_spec = compression_spec
        # The distillation configuration.
        self.distillation_spec = distillation_spec
        # The evaluation configuration.
        self.evaluation_spec = evaluation_spec
        # The additional information.
        self.extra_info = extra_info
        # The model format.
        # - OfflineModel
        # - SavedModel
        # - Keras H5
        # - Frozen Pb
        # - Caffe Prototxt
        # - TorchScript
        # - XGBoost
        # - PMML
        # - AlinkModel
        # - ONNX
        self.format_type = format_type
        # The model framework.
        # - Pytorch
        # - XGBoost
        # - Keras
        # - Caffe
        # - Alink
        # - Xflow
        # - TensorFlow
        self.framework_type = framework_type
        # The UTC time of model creation, in ISO 8601 format.
        self.gmt_create_time = gmt_create_time
        # The UTC time when the model was last updated, in ISO 8601 format.
        self.gmt_modified_time = gmt_modified_time
        # Describes how to apply the model to downstream inference applications, such as specifying the EAS processor or container. Example:
        # `{
        #     "processor": "tensorflow_gpu_1.12"
        # }`
        self.inference_spec = inference_spec
        # The label list.
        self.labels = labels
        # The model metrics.
        self.metrics = metrics
        # The extended fields. JsonString type.
        self.options = options
        # The Alibaba Cloud account ID.
        self.owner_id = owner_id
        # The source ID.
        # 
        # * If the source type is Custom, this field has no restrictions.
        # 
        # * If the source type is PAIFlow or TrainingService, the format is: 
        # ```
        # region=<region_id>,workspaceId=<workspace_id>,kind=<kind>,id=<id>
        # ```
        # region is the Alibaba Cloud region ID. workspaceId is the workspace ID. kind specifies the type. Valid values: PipelineRun (PAI workflow) and ServiceJob (training service). id is the unique identifier.
        self.source_id = source_id
        # The model source type. Default value: Custom.
        # 
        # - Custom: custom.
        # - PAIFlow: PAI workflow.
        # - TrainingService: PAI training service.
        self.source_type = source_type
        # The training configuration. Used for fine-tuning and incremental training.
        self.training_spec = training_spec
        # The model version URI, which specifies the model storage location. This can be an HTTP(S) address of the model, such as `https://myweb.com/mymodel.tar.gz`. If the model is stored in OSS, the format is `oss://<bucket>.<endpoint>/object`. You can query the endpoint in the OSS console. Example: `oss://mybucket.oss-cn-beijing.aliyuncs.com/mypath/`.
        self.uri = uri
        # The user ID.
        self.user_id = user_id
        # The model version description.
        self.version_description = version_description
        # The model version, unique within the model. If not specified, the first version defaults to `0.1.0`, and subsequent versions increment the minor version number by 1. For example, the second version defaults to `0.2.0`.
        # 
        # The version number consists of a major version number, a minor version number, and a stage version number, separated by `.`. The major and minor version numbers are numeric. The stage version number starts with a digit, followed by `_` and letters. Examples: 1.1.0 or 2.3.4_beta.
        # 
        # Regular expression reference: `"^\\d+\\.\\d+\\.\\d+(_\\w+)?$"`
        self.version_name = version_name

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status

        if self.compression_spec is not None:
            result['CompressionSpec'] = self.compression_spec

        if self.distillation_spec is not None:
            result['DistillationSpec'] = self.distillation_spec

        if self.evaluation_spec is not None:
            result['EvaluationSpec'] = self.evaluation_spec

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.format_type is not None:
            result['FormatType'] = self.format_type

        if self.framework_type is not None:
            result['FrameworkType'] = self.framework_type

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.inference_spec is not None:
            result['InferenceSpec'] = self.inference_spec

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.options is not None:
            result['Options'] = self.options

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.training_spec is not None:
            result['TrainingSpec'] = self.training_spec

        if self.uri is not None:
            result['Uri'] = self.uri

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.version_description is not None:
            result['VersionDescription'] = self.version_description

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')

        if m.get('CompressionSpec') is not None:
            self.compression_spec = m.get('CompressionSpec')

        if m.get('DistillationSpec') is not None:
            self.distillation_spec = m.get('DistillationSpec')

        if m.get('EvaluationSpec') is not None:
            self.evaluation_spec = m.get('EvaluationSpec')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')

        if m.get('FrameworkType') is not None:
            self.framework_type = m.get('FrameworkType')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('InferenceSpec') is not None:
            self.inference_spec = m.get('InferenceSpec')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.ModelVersionLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('TrainingSpec') is not None:
            self.training_spec = m.get('TrainingSpec')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class ModelVersionLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the label.
        self.key = key
        # The value of the label.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

