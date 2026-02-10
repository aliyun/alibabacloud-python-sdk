# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePropertyCountResponseBody(DaraModel):
    def __init__(
        self,
        agentless_llm_service: int = None,
        agentless_sca_ai_component: int = None,
        autorun: int = None,
        cron: int = None,
        database: int = None,
        lkm: int = None,
        port: int = None,
        process: int = None,
        request_id: str = None,
        sca: int = None,
        software: int = None,
        user: int = None,
        web: int = None,
        webserver: int = None,
    ):
        # The number of AI services.
        self.agentless_llm_service = agentless_llm_service
        # The number of AI tools.
        self.agentless_sca_ai_component = agentless_sca_ai_component
        # The number of startup items.
        self.autorun = autorun
        # The number of scheduled tasks.
        self.cron = cron
        # The number of databases.
        self.database = database
        # The number of kernel modules.
        self.lkm = lkm
        # The number of ports.
        self.port = port
        # The number of processes.
        self.process = process
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The number of middleware assets.
        self.sca = sca
        # The number of software assets.
        self.software = software
        # The number of accounts.
        self.user = user
        # The number of websites.
        self.web = web
        # The number of web services.
        self.webserver = webserver

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agentless_llm_service is not None:
            result['AgentlessLlmService'] = self.agentless_llm_service

        if self.agentless_sca_ai_component is not None:
            result['AgentlessScaAiComponent'] = self.agentless_sca_ai_component

        if self.autorun is not None:
            result['Autorun'] = self.autorun

        if self.cron is not None:
            result['Cron'] = self.cron

        if self.database is not None:
            result['Database'] = self.database

        if self.lkm is not None:
            result['Lkm'] = self.lkm

        if self.port is not None:
            result['Port'] = self.port

        if self.process is not None:
            result['Process'] = self.process

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sca is not None:
            result['Sca'] = self.sca

        if self.software is not None:
            result['Software'] = self.software

        if self.user is not None:
            result['User'] = self.user

        if self.web is not None:
            result['Web'] = self.web

        if self.webserver is not None:
            result['Webserver'] = self.webserver

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentlessLlmService') is not None:
            self.agentless_llm_service = m.get('AgentlessLlmService')

        if m.get('AgentlessScaAiComponent') is not None:
            self.agentless_sca_ai_component = m.get('AgentlessScaAiComponent')

        if m.get('Autorun') is not None:
            self.autorun = m.get('Autorun')

        if m.get('Cron') is not None:
            self.cron = m.get('Cron')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Lkm') is not None:
            self.lkm = m.get('Lkm')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Sca') is not None:
            self.sca = m.get('Sca')

        if m.get('Software') is not None:
            self.software = m.get('Software')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('Web') is not None:
            self.web = m.get('Web')

        if m.get('Webserver') is not None:
            self.webserver = m.get('Webserver')

        return self

