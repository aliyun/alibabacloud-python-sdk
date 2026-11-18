# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RunAppInstanceCommandRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_ids: List[str] = None,
        app_instance_persistent_id: str = None,
        app_instance_persistent_ids: List[str] = None,
        command_content: str = None,
        command_param: str = None,
        command_type: str = None,
        description: str = None,
        product_type: str = None,
        run_script_type: str = None,
        timeout: int = None,
    ):
        # The ID of the delivery group. This parameter is used to execute commands within a single delivery group. You can call the [ListAppInstanceGroup](~~ListAppInstanceGroup~~) operation to obtain the ID. If AppInstanceGroupIds is not specified, you must specify this parameter. Otherwise, a parameter error is returned. If AppInstanceGroupIds is specified, this parameter does not take effect.
        self.app_instance_group_id = app_instance_group_id
        # The list of delivery group IDs. This parameter is used to issue commands in batches to multiple delivery groups in the same region. The command is executed on all persistent sessions in each delivery group in the list, and only one command execution ID is returned. You can specify up to 100 delivery group IDs. Duplicate IDs are automatically deduplicated. All delivery groups must belong to the same region. Otherwise, the InvalidRegion.NotMatch error is returned. If any delivery group does not exist, the InvalidAppInstanceGroup.NotFound error is returned. If this parameter is specified, AppInstanceGroupId and AppInstancePersistentIds do not take effect.
        self.app_instance_group_ids = app_instance_group_ids
        # The ID of the persistent session. This parameter is used to select a single persistent session within the delivery group specified by AppInstanceGroupId to execute the command. The session must belong to the specified delivery group. Otherwise, an error is returned.
        self.app_instance_persistent_id = app_instance_persistent_id
        # The list of persistent session IDs. This parameter is used to select multiple persistent sessions within the delivery group specified by AppInstanceGroupId to execute the command. You can specify up to 100 session IDs. If AppInstanceGroupIds is specified, this parameter does not take effect, and the command is executed on all persistent sessions in each delivery group.
        self.app_instance_persistent_ids = app_instance_persistent_ids
        # The command content, which is the script content executed in the session. The content must match the script type specified by RunScriptType.
        # 
        # This parameter is required.
        self.command_content = command_content
        # The command parameters, which are passed through to the session execution end along with the command content. Whether to specify this parameter and the specific format depend on the command content. If not required, you can leave this parameter empty.
        self.command_param = command_param
        # The command type. Currently, only CloudAssistantCmd (Cloud Assistant command) is supported. Specifying other values results in a parameter error.
        # 
        # This parameter is required.
        self.command_type = command_type
        # The description of the command. This parameter is used to describe the purpose of the issued command for subsequent identification.
        self.description = description
        # The product type. Currently, only WuyingServer (WUYING Workspace) is supported. Specifying other values results in a parameter error.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The type of the script to execute. Valid values:
        # - RunBatScript: BAT script.
        # - RunPowerShellScript: PowerShell script.
        # - RunShellScript: Shell script.
        # - RunAIAgentScript: AI agent script.
        self.run_script_type = run_script_type
        # The timeout period for command execution, in seconds. If this parameter is not specified, the default value is 60 seconds.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_ids is not None:
            result['AppInstanceGroupIds'] = self.app_instance_group_ids

        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id

        if self.app_instance_persistent_ids is not None:
            result['AppInstancePersistentIds'] = self.app_instance_persistent_ids

        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.command_param is not None:
            result['CommandParam'] = self.command_param

        if self.command_type is not None:
            result['CommandType'] = self.command_type

        if self.description is not None:
            result['Description'] = self.description

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.run_script_type is not None:
            result['RunScriptType'] = self.run_script_type

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupIds') is not None:
            self.app_instance_group_ids = m.get('AppInstanceGroupIds')

        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')

        if m.get('AppInstancePersistentIds') is not None:
            self.app_instance_persistent_ids = m.get('AppInstancePersistentIds')

        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('CommandParam') is not None:
            self.command_param = m.get('CommandParam')

        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RunScriptType') is not None:
            self.run_script_type = m.get('RunScriptType')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

