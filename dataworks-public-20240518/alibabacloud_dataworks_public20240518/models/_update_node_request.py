# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNodeRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        project_id: int = None,
        spec: str = None,
    ):
        # The unique identifier of the Data Studio node.
        # 
        # >  This field is of the Long type in SDK versions prior to 8.0.0, and of the String type in SDK versions 8.0.0 and later. This change does not affect normal SDK usage; the parameter will still be returned according to the type defined in the SDK. However, compilation failures may occur due to the type change only when upgrading the SDK across version 8.0.0. In this case, you must manually update the data type.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # { "title": "CycleWorkflow Schema", "description": "the JSON schema that is used to configure the auto triggered workflow and nodes in the workflow", "type": "object", "required": [ "version", "kind", "spec" ], "properties": { "version": { "type": "string", "const": "1.1.0", "description": "the schema version. The value is fixed to 1.1.0" }, "kind": { "type": "string", "enum": [ "Workflow", "Node" ], "description": "the resource type" }, "spec": { "type": "object", "description": "the key configurations of the workflow", "required": [ "nodes" ], "properties": { "nodes": { "type": "array", "description": "the nodes in the workflow", "items": { "type": "object", "required": [ "name", "script" ], "properties": { "recurrence": { "type": "string", "enum": [ "Normal", "Pause", "Skip", "NoneAuto" ], "description": "the running mode of the node. Valid values: Normal, Pause, Skip, and NoneAuto" }, "id": { "type": "string", "description": "the node ID" }, "timeout": { "type": "integer", "minimum": 0, "description": "the timeout period. Unit: seconds" }, "instanceMode": { "type": "string", "enum": [ "T+1", "Immediately" ], "description": "the instance generation mode. Valid values: T+1 and Immediately" }, "rerunMode": { "type": "string", "enum": [ "Allowed", "Denied", "FailureAllowed" ], "description": "the rerun mode. Valid values: AllAllowed, Denied, and FailureAllowed" }, "rerunTimes": { "type": "integer", "minimum": 0, "description": "the maximum number of reruns allowed after a failure" }, "rerunInterval": { "type": "integer", "minimum": 0, "description": "the rerun interval. Unit: seconds" }, "datasource": { "type": "object", "description": "the configurations of the data source", "required": [ "name", "type" ], "properties": { "name": { "type": "string", "description": "the name of the data source" }, "type": { "type": "string", "enum": [ "odps" ], "description": "the type of the data source. Only MaxCompute data sources are supported" } } }, "script": { "type": "object", "description": "the script configurations of the node", "required": [ "path", "runtime" ], "properties": { "language": { "type": "string", "description": "the programming language of the script" }, "path": { "type": "string", "description": "the storage path of the script file. The storage path ends with the node name and does not require a file extension" }, "runtime": { "type": "object", "description": "the configurations of the runtime environment", "required": [ "command" ], "properties": { "command": { "type": "string", "enum": [ "ODPS_SQL" ], "Description": "the command" }, "cu": { "type": "string", "description": "the unit of the computing resource" } } } } }, "trigger": { "type": "object", "description": "the configurations of the node trigger", "required": [ "type" ], "properties": { "type": { "type": "string", "enum": [ "Scheduler", "Manual", "Streaming", "None" ], "description": "the trigger type. Valid values: Scheduler, Manual, Streaming, and None" }, "cron": { "type": "string", "description": "the cron expression, which is suitable for only auto triggered nodes" }, "startTime": { "type": "string", "format": "yyyy-MM-dd hh:mm:ss", "description": "the start time for scheduling" }, "endTime": { "type": "string", "format": "yyyy-MM-dd hh:mm:ss", "description": "the end time for scheduling" } } }, "runtimeResource": { "type": "object", "description": "the resource configurations for running", "required": [ "resourceGroup" ], "properties": { "resourceGroup": { "type": "string", "description": "the name of the resource group" } } }, "name": { "type": "string", "description": "the name of the node" }, "owner": { "type": "string", "description": "the node owner" }, "inputs": { "type": "object", "description": "the node input parameters", "properties": { "nodeOutputs": { "type": "array", "description": "the node dependencies", "items": { "type": "object", "required": [ "data" ], "properties": { "data": { "type": "string", "description": "the identifier of the node dependency" }, "refTableName": { "type": "string", "description": "the name of the table that is associated with the node. You must configure this parameter if the artifactType parameter is set to Table" }, "isDefault": { "type": "boolean", "description": "specifies whether the table is the default input table“ } } } } } }, "outputs": { "type": "object", "description": "the node output parameters", "properties": { "nodeOutputs": { "type": "array", "description": "the node dependencies", "items": { "type": "object", "required": [ "data" ], "properties": { "data": { "type": "string", "description": "the identifier of the node dependency" }, "refTableName": { "type": "string", "description": "the name of the table that is associated with the node. You must configure this parameter if the artifactType parameter is set to Table" }, "isDefault": { "type": "boolean", "description": "specifies whether the table is the default output table“ } } } } } } } } } } } } }
        # 
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

