"""
Module for the configurations of system
"""
import os


class RestApiServer:
    HOST = os.environ.get("REST_API_HOST") or '0.0.0.0'
    PORT = os.environ.get("REST_API_PORT") or 2808
    API_VERSION = os.environ.get("REST_API_VERSION") or "/app/v0.1"




class Neo4jConfig:
    BOLT = "bolt://0.0.0.0:7687"
    HOST = os.environ.get("NEO4J_HOST") or "165.22.59.25"
    BOTH_PORT = os.environ.get("NEO4J_BOTH_PORT") or 7687
    HTTP_PORT = os.environ.get("NEO4J_HTTP_PORT") or 7474
    HTTPS_PORT = os.environ.get("NEO4J_HTTPS_PORT") or 7473
    NEO4J_USERNAME = os.environ.get("NEO4J_USERNAME") or "neo4j"
    NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD") or "klg_pass"
