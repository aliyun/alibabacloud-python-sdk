# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pailangstudio20240710 import models as main_models
from darabonba.model import DaraModel

class Flow(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        code_mode_run_info: str = None,
        create_from: str = None,
        creator: str = None,
        description: str = None,
        flow_id: str = None,
        flow_name: str = None,
        flow_storage_path: str = None,
        flow_template_id: str = None,
        flow_type: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        runtime: main_models.FlowRuntime = None,
        runtime_id: str = None,
        source_uri: str = None,
        version: str = None,
        work_dir: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.code_mode_run_info = code_mode_run_info
        self.create_from = create_from
        self.creator = creator
        self.description = description
        self.flow_id = flow_id
        self.flow_name = flow_name
        self.flow_storage_path = flow_storage_path
        self.flow_template_id = flow_template_id
        self.flow_type = flow_type
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.runtime = runtime
        self.runtime_id = runtime_id
        self.source_uri = source_uri
        self.version = version
        self.work_dir = work_dir
        self.workspace_id = workspace_id

    def validate(self):
        if self.runtime:
            self.runtime.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.code_mode_run_info is not None:
            result['CodeModeRunInfo'] = self.code_mode_run_info

        if self.create_from is not None:
            result['CreateFrom'] = self.create_from

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.flow_storage_path is not None:
            result['FlowStoragePath'] = self.flow_storage_path

        if self.flow_template_id is not None:
            result['FlowTemplateId'] = self.flow_template_id

        if self.flow_type is not None:
            result['FlowType'] = self.flow_type

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()

        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id

        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri

        if self.version is not None:
            result['Version'] = self.version

        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('CodeModeRunInfo') is not None:
            self.code_mode_run_info = m.get('CodeModeRunInfo')

        if m.get('CreateFrom') is not None:
            self.create_from = m.get('CreateFrom')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('FlowStoragePath') is not None:
            self.flow_storage_path = m.get('FlowStoragePath')

        if m.get('FlowTemplateId') is not None:
            self.flow_template_id = m.get('FlowTemplateId')

        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Runtime') is not None:
            temp_model = main_models.FlowRuntime()
            self.runtime = temp_model.from_map(m.get('Runtime'))

        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class FlowRuntime(DaraModel):
    def __init__(
        self,
        runtime_id: str = None,
        runtime_name: str = None,
        runtime_status: str = None,
        runtime_type: str = None,
        support_ssestream: bool = None,
    ):
        # 运行时ID
        self.runtime_id = runtime_id
        # 运行时名称
        self.runtime_name = runtime_name
        # 运行时状态
        self.runtime_status = runtime_status
        # 运行时类型
        self.runtime_type = runtime_type
        # 是否支持SSE
        self.support_ssestream = support_ssestream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id

        if self.runtime_name is not None:
            result['RuntimeName'] = self.runtime_name

        if self.runtime_status is not None:
            result['RuntimeStatus'] = self.runtime_status

        if self.runtime_type is not None:
            result['RuntimeType'] = self.runtime_type

        if self.support_ssestream is not None:
            result['SupportSSEStream'] = self.support_ssestream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        if m.get('RuntimeName') is not None:
            self.runtime_name = m.get('RuntimeName')

        if m.get('RuntimeStatus') is not None:
            self.runtime_status = m.get('RuntimeStatus')

        if m.get('RuntimeType') is not None:
            self.runtime_type = m.get('RuntimeType')

        if m.get('SupportSSEStream') is not None:
            self.support_ssestream = m.get('SupportSSEStream')

        return self

