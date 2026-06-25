# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModelVersionsRequest(DaraModel):
    def __init__(
        self,
        approval_status: str = None,
        format_type: str = None,
        framework_type: str = None,
        label: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        source_id: str = None,
        source_type: str = None,
        version_name: str = None,
    ):
        # The approval status. This parameter is used to filter the model version list. Valid values:
        # 
        # - Pending: The model version is pending approval.
        # 
        # - Approved: The model version is approved for publishing.
        # 
        # - Rejected: The model version is rejected for publishing.
        self.approval_status = approval_status
        # The model format. This parameter is used to filter the model version list. Valid values:
        # 
        # - OfflineModel
        # 
        # - SavedModel
        # 
        # - Keras H5
        # 
        # - Frozen Pb
        # 
        # - Caffe Prototxt
        # 
        # - TorchScript
        # 
        # - XGBoost
        # 
        # - PMML
        # 
        # - AlinkModel
        # 
        # - ONNX
        self.format_type = format_type
        # The model framework. This parameter is used to filter the model version list. Valid values:
        # 
        # - Pytorch
        #   -XGBoost
        # 
        # - Keras
        # 
        # - Caffe
        # 
        # - Alink
        # 
        # - Xflow
        # 
        # - TensorFlow
        self.framework_type = framework_type
        # The label string. This parameter is used to filter the list. Model versions that have the specified string in the key or value of their labels are returned.
        self.label = label
        # The order in which to sort the entries in the paged query. The default value is ASC.
        # 
        # - ASC: ascending order.
        # 
        # - DESC: descending order.
        self.order = order
        # The page number of the model version list. The value starts from 1. The default value is 1.
        self.page_number = page_number
        # The number of entries to return on each page for a paged query. The default value is 10.
        self.page_size = page_size
        # The field to use for sorting in the paged query. Currently, the GmtCreateTime field is used for sorting.
        self.sort_by = sort_by
        # The source ID.
        # 
        # - If the source type is Custom, this parameter is not restricted.
        # 
        # - If the source is PAIFlow or TrainingService, the format is as follows:
        # 
        # ```
        # region=<region_id>,workspaceId=<workspace_id>,kind=<kind>,id=<id>
        # ```
        # 
        # where:
        # 
        # - region is the Alibaba Cloud region ID.
        # 
        # - workspaceId is the workspace ID.
        # 
        # - kind: the type. Valid values: PipelineRun (PAIFlow pipeline) and ServiceJob (training service).
        # 
        # - id: the unique identifier.
        self.source_id = source_id
        # The source type of the model. This parameter is used to filter the model version list. Valid values:
        # 
        # - Custom (default): a custom model.
        # 
        # - PAIFlow: a model from a PAI pipeline.
        # 
        # - TrainingService: a model from a PAI training service.
        self.source_type = source_type
        # The model version name. This parameter is used to filter the model version list.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status

        if self.format_type is not None:
            result['FormatType'] = self.format_type

        if self.framework_type is not None:
            result['FrameworkType'] = self.framework_type

        if self.label is not None:
            result['Label'] = self.label

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')

        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')

        if m.get('FrameworkType') is not None:
            self.framework_type = m.get('FrameworkType')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

