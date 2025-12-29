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
        # This parameter is required.
        self.app_id = app_id
        self.command = command
        self.command_args = command_args
        self.envs = envs
        self.event_id = event_id
        # The arguments in the JAR package. The arguments are used to start the job. The default startup command is `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`.
        self.jar_start_args = jar_start_args
        # The option settings in the JAR package. The settings are used to start the job. The default startup command is `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArg`.
        self.jar_start_options = jar_start_options
        # The number of concurrent instances.
        self.replicas = replicas
        # The time at which the job is triggered. Format: `yyyy-MM-dd\\"T\\"HH:mm:ss\\"Z\\"`.
        self.time = time
        # The startup command of the WAR package. For information about how to configure the startup command, see [Configure a startup command](https://help.aliyun.com/document_detail/96677.html).
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

