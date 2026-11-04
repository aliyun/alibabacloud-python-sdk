# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecJobRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        command: str = None,
        command_args: str = None,
        envs: str = None,
        event_id: str = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        replicas: str = None,
        time: str = None,
        war_start_options: str = None,
    ):
        # The ID of the job template.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The image startup command. The command must be an executable object that exists in the container. Example:
        # 
        # ```
        # command:
        #       - echo
        #       - abc
        #       - >
        #       - file0
        # ```
        # Based on the preceding example, Command="echo" and CommandArgs=["abc", ">", "file0"].
        self.command = command
        # The arguments for the image startup command. These are the arguments required by the **Command** startup command. Format:
        # 
        # `["a","b"]`
        # 
        # In the preceding example, CommandArgs=["abc", ">", "file0"]. The ["abc", ">", "file0"] part must be converted to a string in JSON array format. If this parameter is not required, leave it empty.
        self.command_args = command_args
        # The environment variables for the container. You can customize environment variables or reference configuration items. To reference a configuration item, you must first create a ConfigMap instance. For more information, see [CreateConfigMap](https://help.aliyun.com/document_detail/176914.html). Valid values:
        # - Custom configuration
        #     - **name**: the name of the environment variable.
        #     - **value**: the value of the environment variable.
        # - Referenced configuration items
        #     - **name**: the name of the environment variable. You can reference a single key or all keys. To reference all keys, enter sae-sys-configmap-all-<configuration item name>, for example, sae-sys-configmap-all-test1.
        #     - **valueFrom**: the reference of the environment variable. Set the value to configMapRef.
        #     - **configMapId**: the ID of the configuration item.
        #     - **key**: the key. If you reference all key-value pairs, do not set this field.
        self.envs = envs
        # The event ID. This parameter is user-defined and used for idempotence. Only one job is created for the same event ID.
        self.event_id = event_id
        # The startup arguments for the JAR package job. Default job startup command:
        # `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`
        self.jar_start_args = jar_start_args
        # The startup options for the JAR package job. Default job startup command:
        # `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArg`
        self.jar_start_options = jar_start_options
        # The number of concurrent instances for the job.
        self.replicas = replicas
        # The time when the job is triggered. Format: `yyyy-MM-dd\\"T\\"HH:mm:ss\\"Z\\"`.
        self.time = time
        # The startup command for the WAR package deployment job. The configuration procedure is the same as that for the image deployment startup command. For more information, see [Configure a startup command](https://help.aliyun.com/document_detail/96677.html).
        self.war_start_options = war_start_options

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.command is not None:
            result['Command'] = self.command

        if self.command_args is not None:
            result['CommandArgs'] = self.command_args

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args

        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.time is not None:
            result['Time'] = self.time

        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')

        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')

        return self

