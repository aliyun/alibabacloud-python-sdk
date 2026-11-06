# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAdaptorShrinkRequest(DaraModel):
    def __init__(
        self,
        adaptor_id: str = None,
        app_script: str = None,
        execute_file_address: str = None,
        optimize_param: str = None,
        silence_param: str = None,
        user_config_shrink: str = None,
    ):
        # The ID of the application adapter to be modified. This parameter is required and must belong to an application adapter manageable by the current account.
        self.adaptor_id = adaptor_id
        # **Not enabled. Do not pass this parameter.** This parameter does not support modifying application scripts.
        # 
        # The example "Not applicable (not enabled)" is only a description of the field status and is not a valid parameter value.
        self.app_script = app_script
        # **Not enabled. Do not pass this parameter.** This parameter does not support modifying executable file paths.
        # 
        # The example "Not applicable (not enabled)" is only a description of the field status and is not a valid parameter value.
        self.execute_file_address = execute_file_address
        # The application optimization configuration, represented as a JSON object string. Pass this parameter only when specific optimization configuration requirements exist. The content must be a valid JSON object.
        self.optimize_param = optimize_param
        # The command-line parameters used when the application starts. If this parameter is not empty, it is used to update the startup parameters of the application adapter. Specify the parameters based on the startup requirements of the application.
        self.silence_param = silence_param
        # The application runtime configuration object. If this parameter is omitted, the existing user configuration is not modified.
        # 
        # **If this parameter is passed, the original UserConfig is completely replaced and not merged item by item.** Submit the complete configuration and include the configuration items that need to be retained. Subfields that are not provided do not automatically inherit the original values.
        self.user_config_shrink = user_config_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adaptor_id is not None:
            result['AdaptorId'] = self.adaptor_id

        if self.app_script is not None:
            result['AppScript'] = self.app_script

        if self.execute_file_address is not None:
            result['ExecuteFileAddress'] = self.execute_file_address

        if self.optimize_param is not None:
            result['OptimizeParam'] = self.optimize_param

        if self.silence_param is not None:
            result['SilenceParam'] = self.silence_param

        if self.user_config_shrink is not None:
            result['UserConfig'] = self.user_config_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptorId') is not None:
            self.adaptor_id = m.get('AdaptorId')

        if m.get('AppScript') is not None:
            self.app_script = m.get('AppScript')

        if m.get('ExecuteFileAddress') is not None:
            self.execute_file_address = m.get('ExecuteFileAddress')

        if m.get('OptimizeParam') is not None:
            self.optimize_param = m.get('OptimizeParam')

        if m.get('SilenceParam') is not None:
            self.silence_param = m.get('SilenceParam')

        if m.get('UserConfig') is not None:
            self.user_config_shrink = m.get('UserConfig')

        return self

