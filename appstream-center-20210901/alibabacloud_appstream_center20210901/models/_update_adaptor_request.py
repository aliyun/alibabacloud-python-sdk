# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class UpdateAdaptorRequest(DaraModel):
    def __init__(
        self,
        adaptor_id: str = None,
        app_script: str = None,
        execute_file_address: str = None,
        optimize_param: str = None,
        silence_param: str = None,
        user_config: main_models.UpdateAdaptorRequestUserConfig = None,
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
        self.user_config = user_config

    def validate(self):
        if self.user_config:
            self.user_config.validate()

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

        if self.user_config is not None:
            result['UserConfig'] = self.user_config.to_map()

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
            temp_model = main_models.UpdateAdaptorRequestUserConfig()
            self.user_config = temp_model.from_map(m.get('UserConfig'))

        return self

class UpdateAdaptorRequestUserConfig(DaraModel):
    def __init__(
        self,
        disconnect_action: str = None,
        fixed_resolution: str = None,
        show_window: str = None,
    ):
        # The processing policy after a connection is disconnected. When modifying other UserConfig configurations, if you need to retain the original policy, pass the original value in the complete configuration object. This operation does not automatically populate default values.
        self.disconnect_action = disconnect_action
        # The fixed resolution used when the application runs, in the format of width × height, in pixels.
        self.fixed_resolution = fixed_resolution
        # The application window display configuration. When modifying other UserConfig configurations, if you need to retain the original configuration, pass the original value in the complete configuration object. This operation does not automatically populate default values.
        self.show_window = show_window

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disconnect_action is not None:
            result['DisconnectAction'] = self.disconnect_action

        if self.fixed_resolution is not None:
            result['FixedResolution'] = self.fixed_resolution

        if self.show_window is not None:
            result['ShowWindow'] = self.show_window

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisconnectAction') is not None:
            self.disconnect_action = m.get('DisconnectAction')

        if m.get('FixedResolution') is not None:
            self.fixed_resolution = m.get('FixedResolution')

        if m.get('ShowWindow') is not None:
            self.show_window = m.get('ShowWindow')

        return self

