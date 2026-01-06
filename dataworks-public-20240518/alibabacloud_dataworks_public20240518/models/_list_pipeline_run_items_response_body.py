# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListPipelineRunItemsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListPipelineRunItemsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # Pagination information.
        self.paging_info = paging_info
        # The request ID. You can use this ID to troubleshoot issues if errors occur.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListPipelineRunItemsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPipelineRunItemsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pipeline_run_items: List[main_models.ListPipelineRunItemsResponseBodyPagingInfoPipelineRunItems] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The list of deployments.
        self.pipeline_run_items = pipeline_run_items
        # The total number of entries that match the conditions.
        self.total_count = total_count

    def validate(self):
        if self.pipeline_run_items:
            for v1 in self.pipeline_run_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PipelineRunItems'] = []
        if self.pipeline_run_items is not None:
            for k1 in self.pipeline_run_items:
                result['PipelineRunItems'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.pipeline_run_items = []
        if m.get('PipelineRunItems') is not None:
            for k1 in m.get('PipelineRunItems'):
                temp_model = main_models.ListPipelineRunItemsResponseBodyPagingInfoPipelineRunItems()
                self.pipeline_run_items.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPipelineRunItemsResponseBodyPagingInfoPipelineRunItems(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        id: str = None,
        message: str = None,
        modify_time: int = None,
        name: str = None,
        spec: str = None,
        status: str = None,
        type: str = None,
        version: int = None,
    ):
        # The deployment creation time.
        self.create_time = create_time
        # The unique identifier of the deployment.
        # 
        # >  Prior to SDK version 8.0.0, this field is of type Long. In SDK version 8.0.0 and later, it is of type String. This change does not affect the normal use of the SDK. The parameter is returned based on the type defined in the SDK. Compilation failures caused by the type change may occur only when you upgrade the SDK across version 8.0.0. In this case, you must manually update the data type.
        self.id = id
        # The error message if the deployment failed.
        self.message = message
        # The time when the deployment was last modified.
        self.modify_time = modify_time
        # The deployment name.
        self.name = name
        # The FlowSpec information describing this deployment. For detailed specifications, see [FlowSpec](https://github.com/aliyun/dataworks-spec/blob/master/README_zh_CN.md).
        self.spec = spec
        # The deployment status. Valid values:
        # 
        # *   Init: Initializing
        # *   Running
        # *   Success
        # *   Fail
        # *   Termination
        self.status = status
        # The deployment type. Valid values:
        # 
        # *   Node
        # *   WorkflowDefinition: Workflow definition.
        # *   Resource
        # *   Function: The object is a function.
        self.type = type
        # The deployment version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

