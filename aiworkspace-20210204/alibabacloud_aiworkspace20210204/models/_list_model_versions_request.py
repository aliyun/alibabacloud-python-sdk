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
        # The approval status based on which the model versions are queried. Valid values:
        # 
        # *   Pending
        # *   Approved
        # *   Rejected
        self.approval_status = approval_status
        # The model format used to filter model versions. Valid values:
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
        # The framework used to filter model versions.
        # 
        # *   Pytorch -XGBoost
        # *   Keras
        # *   Caffe
        # *   Alink
        # *   Xflow
        # *   TensorFlow
        self.framework_type = framework_type
        # The label. Model versions whose label key or label value contains a specific label are filtered.
        self.label = label
        # The order in which the entries are sorted by the specific field on the returned page. Default value: ASC.
        # 
        # *   ASC
        # *   DESC
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The field used to sort the results. The GmtCreateTime field is used for sorting.
        self.sort_by = sort_by
        # The source ID.
        # 
        # *   If the source type is Custom, this field is not limited.
        # *   If the source type is PAIFlow or TrainingService, the format is:
        # 
        # <!---->
        # 
        #     region=<region_id>,workspaceId=<workspace_id>,kind=<kind>,id=<id>
        # 
        # Take note of the following parameters:
        # 
        # *   region is the region ID.
        # *   workspaceId is the ID of the workspace.
        # *   kind is the type. Valid values: PipelineRun (PAIFlow) and ServiceJob (training service).
        # *   id is a unique identifier.
        self.source_id = source_id
        # The source type used to filter model versions. Valid values:
        # 
        # *   Custom (default)
        # *   PAIFlow
        # *   TrainingService
        self.source_type = source_type
        # The model version used to filter model versions.
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

