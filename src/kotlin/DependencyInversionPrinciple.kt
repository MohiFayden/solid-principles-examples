package kotlin

// Abstraction
interface DataSource {
    fun fetchData()
}

// Low-level module
class BackendService : DataSource {
    override fun fetchData() {
        println("Getting data from the database...")
    }
}

// High-level module
class ReportGenerator(private val dataSource: DataSource) {
    fun generateReport() {
        dataSource.fetchData()
        println("Generating report...")
    }
}

// Usage
fun main() {
    val service = BackendService()
    val report = ReportGenerator(service)
    report.generateReport()
}
