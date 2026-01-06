# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class CreateModelVersionRequest(DaraModel):
    def __init__(
        self,
        approval_status: str = None,
        compression_spec: Dict[str, Any] = None,
        distillation_spec: Dict[str, Any] = None,
        evaluation_spec: Dict[str, Any] = None,
        extra_info: Dict[str, Any] = None,
        format_type: str = None,
        framework_type: str = None,
        inference_spec: Dict[str, Any] = None,
        labels: List[main_models.Label] = None,
        metrics: Dict[str, Any] = None,
        options: str = None,
        source_id: str = None,
        source_type: str = None,
        training_spec: Dict[str, Any] = None,
        uri: str = None,
        version_description: str = None,
        version_name: str = None,
    ):
        # The approval status. Valid values:
        # 
        # *   Pending
        # *   Approved
        # *   Rejected
        self.approval_status = approval_status
        # The compression configuration.
        self.compression_spec = compression_spec
        self.distillation_spec = distillation_spec
        # The evaluation configuration.
        self.evaluation_spec = evaluation_spec
        # The additional information.
        self.extra_info = extra_info
        # The model format. Valid values:
        # 
        # *   OfflineModel
        # *   SavedModel
        # *   Keras H5
        # *   Frozen Pb
        # *   Caffe Prototxt
        # *   TorchScript
        # *   XGBoost
        # *   PMML
        # *   AlinkModel
        # *   ONNX
        self.format_type = format_type
        # The model framework. Valid values:
        # 
        # *   Pytorch
        # *   XGBoost
        # *   Keras
        # *   Caffe
        # *   Alink
        # *   Xflow
        # *   TensorFlow
        self.framework_type = framework_type
        # Describes how to apply to downstream inference services. For example, describe the processor and container of EAS. Example: `{ "processor": "tensorflow_gpu_1.12" }`
        self.inference_spec = inference_spec
        # The labels.
        self.labels = labels
        # The metrics for the model. The length after serialization is limited to 8,192.
        self.metrics = metrics
        # The extended field. This is a JSON string.
        self.options = options
        # The ID of the model source.
        # 
        # *   If SourceType is set to Custom, this parameter is not limited.
        # *   If SourceType is set to PAIFlow or TrainingService, the ID of the model source is in the following format:
        # 
        # <!---->
        # 
        #     region=<region_id>,workspaceId=<workspace_id>,kind=<kind>,id=<id>
        # 
        # Take note of the following parameters:
        # 
        # *   region indicates the region ID.
        # *   workspaceId indicates the workspace ID.
        # *   kind indicates the type. Valid values: PipelineRun (PAIFlow) and ServiceJob (training service).
        # *   id indicates the unique identifier.
        self.source_id = source_id
        # The type of the model source. Valid values:
        # 
        # *   Custom (default)
        # *   PAIFlow
        # *   TrainingService: the Platform for AI (PAI) training service.
        self.source_type = source_type
        # The training configurations, which is used for fine-tuning and incremental training.
        self.training_spec = training_spec
        # The URI of the model version, which is the location where the model is stored. Valid values:
        # 
        # *   The HTTP(S) address of the model. Example: `https://myweb.com/mymodel.tar.gz`.
        # *   The OSS path of the model, in the format of `oss://<bucket>.<endpoint>/object`. For information about endpoints, see [OSS regions and endpoints](https://help.aliyun.com/document_detail/31837.html). Example: `oss://mybucket.oss-cn-beijing.aliyuncs.com/mypath/`.
        # 
        # This parameter is required.
        self.uri = uri
        # The version description.
        self.version_description = version_description
        # The model version, which is unique for each model. If you leave this parameter empty, the first version is **0.1.0** by default. After that, the minor version number is increased by 1 in sequence. For example, the second version number is **0.2.0**. A version number consists of a major version number, a minor version number, and a stage version number, separated by periods (.). The major version number and minor version number are numeric. The stage version number begins with a digit and can include numbers, underscores, and letters. For example, the version number is 1.1.0 or 2.3.4_beta.
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

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.training_spec is not None:
            result['TrainingSpec'] = self.training_spec

        if self.uri is not None:
            result['Uri'] = self.uri

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

        if m.get('InferenceSpec') is not None:
            self.inference_spec = m.get('InferenceSpec')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('TrainingSpec') is not None:
            self.training_spec = m.get('TrainingSpec')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

