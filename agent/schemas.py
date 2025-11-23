from pydantic import BaseModel, Field


class FileSchema(BaseModel):
    path: str = Field(description="The path to the file to be created or modified")
    purpose: str = Field(
        description="The purpose of the file, e.g 'main application logic', 'data processing module', etc"
    )


class PlanSchema(BaseModel):
    name: str = Field(description="The name of app to be built")
    description: str = Field(
        description="A one-line description of the app to be build, e.g. 'A web application for managing personal finances'"
    )
    techstack: list = Field(
        description="The tech stack to be used while building the app, e.g. 'Python','Javascript',  'react', 'flask',etc"
    )
    features: list = Field(
        description="A list of feaature that the app should have e.g. 'user_authentication', 'data_visualization',etc"
    )
    files: list[FileSchema] = Field(
        description="Alist of file to be created , each with a 'path', and 'purpose'."
    )
