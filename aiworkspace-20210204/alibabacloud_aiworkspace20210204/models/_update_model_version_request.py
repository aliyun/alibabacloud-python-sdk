# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateModelVersionRequest(DaraModel):
    def __init__(
        self,
        approval_status: str = None,
        compression_spec: Dict[str, Any] = None,
        distillation_spec: Dict[str, Any] = None,
        evaluation_spec: Dict[str, Any] = None,
        extra_info: Dict[str, Any] = None,
        inference_spec: Dict[str, Any] = None,
        metrics: Dict[str, Any] = None,
        options: str = None,
        source_id: str = None,
        source_type: str = None,
        training_spec: Dict[str, Any] = None,
        version_description: str = None,
    ):
        # The approval status. Valid values:
        # 
        # - Pending: The model is pending approval.
        # 
        # - Approved: The model is approved to be published.
        # 
        # - Rejected: The model is not approved to be published.
        self.approval_status = approval_status
        # The compression configuration.
        self.compression_spec = compression_spec
        # The distillation configuration.
        self.distillation_spec = distillation_spec
        # The evaluation configuration.
        self.evaluation_spec = evaluation_spec
        # Other information.
        self.extra_info = extra_info
        # Describes how to apply the model to downstream inference applications. For example, describe the processor and container for Elastic Algorithm Service (EAS). Example:
        # `{ "processor": "tensorflow_gpu_1.12" }`.
        self.inference_spec = inference_spec
        # The model metrics.
        # The length cannot exceed 8,192 characters after serialization.
        self.metrics = metrics
        # The extended field. This field is a JSON string.
        self.options = options
        # The source ID.
        # 
        # - If the source type is Custom, this field has no restrictions.
        # 
        # - If the source is PAIFlow or TrainingService, the format is as follows:
        # 
        # ```
        # region=<region_id>,workspaceId=<workspace_id>,kind=<kind>,id=<id>
        # ```
        # 
        # The parameters are described as follows:
        # 
        # - region: the Alibaba Cloud region ID.
        # 
        # - workspaceId: the workspace ID.
        # 
        # - kind: the type. Valid values: PipelineRun (PAI pipeline) or ServiceJob (training service).
        # 
        # - id: the unique identifier.
        self.source_id = source_id
        # The source type of the model. Valid values:
        # 
        # - Custom (default): The model is a custom model.
        # 
        # - PAIFlow: The model is from a PAI pipeline.
        # 
        # - TrainingService: The model is from a PAI training service.
        self.source_type = source_type
        # The training configuration. This is used for fine-tuning and incremental training.
        self.training_spec = training_spec
        # The description of the model version.
        self.version_description = version_description

    def validate(self):
        pass

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

        if self.inference_spec is not None:
            result['InferenceSpec'] = self.inference_spec

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

        if self.version_description is not None:
            result['VersionDescription'] = self.version_description

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

        if m.get('InferenceSpec') is not None:
            self.inference_spec = m.get('InferenceSpec')

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

        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')

        return self

