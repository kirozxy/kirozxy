'''kotlin
data class MySelf(
    val nationality: String = "Vietnamese",
    val pronouns: List<String> = listOf("He", "Him"),
    val askMeAbout: List<String> = listOf(
        "webdev", "reactjs dev", "front-end dev", "html",
        "css", "javascript", "typescript", "graphql", "mysql", "mongodb", "nestjs", "expressjs", "golang"
    ),
    val technologies: Technologies = Technologies(),
    val experience: String = "I have more than 3 years and work in software development."
)

data class Technologies(
    val frontEnd: FrontEnd = FrontEnd(),
    val backEnd: BackEnd = BackEnd(),
    val databases: List<String> = listOf("MySQL", "MongoDb")
)

data class FrontEnd(
    val js: List<String> = listOf("react"),
    val css: List<String> = listOf("antd", "bootstrap")
)

data class BackEnd(
    val js: List<String> = listOf("graphql", "express", "nest"),
    val etclang: List<String> = listOf("golang"),
    val misc: List<String> = listOf("windows", "ubuntu", "docker")
)

val mySelf = MySelf()
'''
